import argparse
from tqdm import tqdm
from word_loader import load_words
from trie import build_trie
from solver import play_hangman
from multiprocessing import Pool, cpu_count, Manager, Process

def progress_monitor(total_items, progress_queue):
    """Monitor progress and print status using tqdm."""
    with tqdm(total=total_items, desc="Processing words") as pbar:
        processed_count = 0
        while processed_count < total_items:
            processed_count += progress_queue.get()
            pbar.update(1)

def process_word(args):
    """Wrapper function to process a single word in parallel and update progress."""
    word, all_words, trie, max_wrong, verbose, progress_queue = args
    result = play_hangman(word, all_words, trie, max_wrong, verbose)
    progress_queue.put(1)
    return result

def process_batch(batch):
    """Process a batch of words in parallel."""
    return [process_word(args) for args in batch]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", type=str, help="Run the script for a specific word instead of the whole list.")
    parser.add_argument("--max_wrong", type=int, default=9, help="Set the maximum number of wrong guesses (default: 9).")
    parser.add_argument("--no_parallel", action="store_true", help="Disable multiprocessing for debugging.")
    args = parser.parse_args()
    
    filename = "filtered_words.txt"
    all_words = load_words(filename)
    
    verbose = bool(args.word)
    word_list = [args.word.lower()] if args.word else all_words
    
    trie = build_trie(tqdm(all_words, desc="Building Trie"))
    
    max_wrong_guesses_required = 0
    results = []

    batch_size = max(1, len(word_list) // cpu_count())
    batches = [word_list[i:i + batch_size] for i in range(0, len(word_list), batch_size)]

    if args.no_parallel:
        results = [process_word((word, all_words, trie, args.max_wrong, verbose)) for word in tqdm(word_list, desc="Processing words")]
    else:
        with Manager() as manager:
            progress_queue = manager.Queue()
            monitor_process = Process(target=progress_monitor, args=(len(word_list), progress_queue))
            monitor_process.start()
            
            with Pool(cpu_count()) as pool:
                results = list(pool.imap(process_batch, 
                    [[(word, all_words, trie, args.max_wrong, verbose, progress_queue) for word in batch] for batch in batches]))

            monitor_process.join()

            # Flatten results since each batch returns a list of results
            results = [item for sublist in results for item in sublist]
    
    for _, _, _, _, wrong_guesses in results:
        max_wrong_guesses_required = max(max_wrong_guesses_required, wrong_guesses)
    
    print(f"Maximum wrong guesses allowed: {args.max_wrong}")
    print(f"Maximum number of wrong guesses needed: {max_wrong_guesses_required}")
    
    if any(not winnable for _, winnable, _, _, _ in results):
        print("There is at least one word that cannot always be won in Hangman.")
        for word, winnable, guess_sequence, remaining_possible_words, wrong_guesses in results:
            if not winnable:
                required_wrong_guesses = len([g for g in guess_sequence if g not in word])
                print(f"Unwinnable word: {word} (Wrong guesses required: {required_wrong_guesses})")
                highlighted_guesses = [
                    f"\033[92m{g}\033[0m" if g in word else f"\033[91m{g}\033[0m"
                    for g in guess_sequence
                ]
                print(f"Guesses made: {', '.join(highlighted_guesses)}")
                print(f"Remaining possible words: {', '.join(remaining_possible_words)}")
    else:
        print("There exists a winning strategy for Hangman with the given word list.")
    
    if verbose:
        print("Verbose mode enabled. Debugging details:")
        for word, winnable, guess_sequence, remaining_possible_words, wrong_guesses in results:
            print(f"Word: {word}")
            print(f"Winnable: {'Yes' if winnable else 'No'}")
            print(f"Guesses made: {', '.join(guess_sequence)}")
            print(f"Remaining possible words: {', '.join(remaining_possible_words) if remaining_possible_words else 'No remaining words'}")
            print(f"Wrong guesses: {wrong_guesses}\n")