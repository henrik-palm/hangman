def initialize_known_letters(word):
    """Automatically reveal spaces, hyphens, and apostrophes in the word at the start of the game."""
    return {char for char in word if char in {' ', '-', '\''}}