from frequency import compute_letter_frequencies, best_letter
from utils import initialize_known_letters
from trie import Trie

def play_hangman_batch(batch):
    """Process a batch of words in parallel to reduce multiprocessing overhead."""
    results = []
    for word, words, trie, cached_freqs, max_wrong_guesses, verbose in batch:
        results.append(play_hangman(word, words, trie, max_wrong_guesses, verbose=False))
    return results

def play_hangman(word, words, trie, max_wrong_guesses, verbose=False):
    """Simulate Hangman and determine if there is a winning strategy (case insensitive)."""
    word = word.lower()
    guessed = initialize_known_letters(word)
    pattern = [char if char in guessed else "_" for char in word]
    wrong_guesses = 0
    guess_sequence = []
    
    remaining_words = sorted(trie.search_pattern(pattern, guessed))

    while "_" in pattern and wrong_guesses < max_wrong_guesses:
        best_guess = best_letter(remaining_words, words, pattern, guessed)  # Pass pattern

        if verbose:
            freqs = compute_letter_frequencies(remaining_words, pattern, guessed)
            print("--------------------------------------------------")
            print(f"Choosing best letter... Picked \"{best_guess}\" (appears in {freqs.get(best_guess, 0)} remaining words)")
            print(f"Current pattern: {''.join(pattern)}")
            print(f"Wrong guesses so far: {wrong_guesses}")
            print(f"Remaining possible words: {', '.join(remaining_words) if remaining_words else 'No remaining words'}")
            print(f"Letter frequency in remaining possible words: {dict(sorted(freqs.items(), key=lambda item: item[1], reverse=True))}")
            print("--------------------------------------------------\n")

        if not best_guess:
            break
        guessed.add(best_guess.lower())
        guess_sequence.append(best_guess.lower())
        
        if best_guess in word:
            pattern = [letter if letter in guessed else "_" for letter in word]  # Update pattern
        else:
            wrong_guesses += 1

        remaining_words = trie.search_pattern(pattern, guessed)
    
    return word, (wrong_guesses < max_wrong_guesses), guess_sequence, remaining_words, wrong_guesses