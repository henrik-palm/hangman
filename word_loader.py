import mmap
import pickle

def load_words_from_file(filename):
    """Load words from a text file using memory-mapped file (mmap) for efficiency."""
    words = []
    with open(filename, "r", encoding="ISO-8859-1") as file:
        with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            for line in iter(mm.readline, b""):
                words.append(line.decode("ISO-8859-1").strip().lower())
    return words

def save_word_list_pickle(filename, words):
    """Save the word list to a pickle file for fast loading."""
    with open(filename, "wb") as f:
        pickle.dump(words, f)

def load_word_list_pickle(filename):
    """Load the word list from a pickle file."""
    with open(filename, "rb") as f:
        return pickle.load(f)

def load_words(filename, pickle_filename="filtered_words.pkl"):
    """Load words from Pickle if available, otherwise from the text file and save to Pickle."""
    try:
        return load_word_list_pickle(pickle_filename)
    except FileNotFoundError:
        words = load_words_from_file(filename)
        save_word_list_pickle(pickle_filename, words)
        return words