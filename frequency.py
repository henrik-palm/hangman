import collections
import functools
import numpy as np
import heapq

_frequency_cache = {}
 
# Global cache for letter frequencies across all words
_global_frequency_cache = {}

def compute_letter_frequencies(words, pattern, guessed):
    """
    Compute letter frequencies for a given word list, considering only letters
    that match the pattern and have not been guessed.
    """
    cache_key = (tuple(pattern), frozenset(sorted(guessed)))
    if cache_key in _frequency_cache:
        return _frequency_cache[cache_key]

    unique_letters = set("".join(words)) - {'-', "\'", ' '}
    letter_indices = {letter: i for i, letter in enumerate(sorted(unique_letters))}
    letter_counts = np.zeros(len(letter_indices), dtype=int)

    for word in words:
        if not matches_pattern(word, pattern, guessed):
            continue
        for letter in set(word) - guessed:
            if letter in letter_indices:
                letter_counts[letter_indices[letter]] += 1

    freq = {letter: int(letter_counts[i]) for letter, i in letter_indices.items() if letter_counts[i] > 0}
    _frequency_cache[cache_key] = freq
    return freq

def matches_pattern(word, pattern, guessed):
    """
    Check if a word matches the given pattern while considering guessed letters.
    """
    if len(word) != len(pattern):
        return False
    return all(p == "_" or p == w for p, w in zip(pattern, word))

def compute_global_frequencies(words):
    """Compute global letter frequencies across all words and cache the result."""
    words_key = frozenset(sorted(words))
    if words_key in _global_frequency_cache:
        return _global_frequency_cache[words_key]

    unique_letters = set("".join(words)) - {'-', "\'", ' '}
    letter_indices = {letter: i for i, letter in enumerate(sorted(unique_letters))}
    letter_counts = np.zeros(len(letter_indices), dtype=int)

    for word in words:
        for letter in set(word):
            if letter in letter_indices:
                letter_counts[letter_indices[letter]] += 1

    global_freqs = {letter: int(letter_counts[i]) for letter, i in letter_indices.items() if letter_counts[i] > 0}
    _global_frequency_cache[words_key] = global_freqs
    return global_freqs

def best_letter(remaining_words, words, pattern, guessed):
    """
    Select the most common unknown letter from the remaining words, ensuring it
    exists in at least one remaining word and follows the pattern.
    """
    if not remaining_words:
        return None

    freqs = compute_letter_frequencies(remaining_words, pattern, guessed)
    global_freqs = compute_global_frequencies(words)

    # Filter out letters that have already been guessed
    available_letters = {l for l in freqs if l not in guessed and freqs[l] > 0}

    # Use heap to find the letter with the highest frequency efficiently
    best_letters = heapq.nlargest(1, available_letters, key=lambda l: (freqs[l], global_freqs[l]))

    return best_letters[0] if best_letters else None