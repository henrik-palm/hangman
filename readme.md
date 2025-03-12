

# Hangman Solver
 
This is a **Hangman solver** implemented in Python. It uses **trie-based word searching** and **letter frequency analysis** to determine the best strategy for guessing words in a game of Hangman. The solver can evaluate a batch of words in parallel and determine whether a winning strategy exists for each word.
 
## Features
 
- **Efficient Trie-based word lookup** to quickly find words matching a pattern.
- **Letter frequency analysis** to determine the most optimal guesses.
- **Parallel processing support** to handle large word lists efficiently.
- **Customizable maximum wrong guesses** to simulate different difficulty levels.
 - **Verbose mode** for debugging and detailed output.
 
 ## Heuristics and Frequency-Based Guessing
 
 The Hangman solver uses **letter frequency analysis** to optimize guesses. The approach follows these heuristics:
 
 1. **Global Letter Frequency**: The solver first computes the frequency of each letter across all words in the dataset. This helps determine which letters are generally more common.
 2. **Pattern-Based Letter Frequency**: When playing Hangman, the solver only considers words that match the current revealed pattern. It calculates letter frequencies for the subset of words that still fit.
 3. **Optimal Letter Selection**: The solver prioritizes letters that:
    - Appear most frequently in the remaining possible words.
    - Have not yet been guessed.
    - Are also common in the overall dataset.
 
 4. **Efficient Lookups with a Trie**: To quickly find valid words that fit the pattern, the solver uses a **Trie data structure**. This speeds up searches and ensures that letter frequency calculations remain efficient.
 
 By combining **global** and **context-specific** letter frequency analysis, the solver makes **intelligent guesses** that minimize wrong attempts and maximize revealed letters.
 
 ## Installation
 
### Prerequisites
 
- Python 3.7+
- `pip` package manager
 
### Install dependencies
 
Run:
 
```sh
pip install -r requirements.txt
```
 
## Usage
 
### Running the Solver
 
To analyze a specific word:
 
```sh
python main.py --word "example"
```
 
To analyze all words in the dataset:
 
```sh
python main.py
```
 
To set a custom maximum number of wrong guesses (default: 9):
 
```sh
python main.py --max_wrong 6
```
 
To **disable multiprocessing** (useful for debugging):
 
```sh
python main.py --no_parallel
```
 
### Output
 
The solver will output:
- The maximum number of wrong guesses required.
- Whether a winning strategy exists for each word.
- The sequence of guesses made.
- The remaining possible words.
 
Example output:
 
```
Maximum number of wrong guesses required: 7
There exists a winning strategy for Hangman with the given word list.
```
 
If a word is **unwinnable**, it will print details:
 
```
Unwinnable word: puzzle
Guesses made: e, a, i, o, u, s, t
Remaining possible words: buzzer, pizzle
```
 
## Playing the Hangman Game

The Hangman solver also includes an interactive game mode. You can play the game by running:

```sh
python main.py --play
```

This will start a new game using a randomly selected word from the dataset. If you want to play with a specific word, provide it as an argument:

```sh
python main.py --play "byboer"
```

### Game Features:

- **Interactive Gameplay**: The game will track guessed letters, incorrect attempts, and display Hangman visuals.
- **Hints Available**: Type `"help"` during the game to receive a hint about the best letter to guess, based on the solver's logic.
- **Revealed Characters**: Certain known characters (`" "`, `"-"`, and `"'"`) are automatically revealed at the start of the game.

The game will continue until you either guess the word correctly or run out of attempts.

## Filtering Words

To filter words from a dataset:

```sh
python filter-ordnet.py
```

This script processes a word list and removes words that:
- Contain numbers.
- Include special characters (except for allowed ones like hyphens and apostrophes).
- Have fewer than five unique letters.

By default, it reads from `words.txt` and outputs:
- `filtered_words.txt` (words that meet the criteria).
- `removed_words.txt` (words that were excluded).

You can modify the input file name in `filter-ordnet.py` if needed.

## File Structure
 
- `main.py` – Handles user input, parallel processing, and running the solver.
- `solver.py` – Core Hangman solving logic.
- `frequency.py` – Computes letter frequencies and determines the best letter to guess.
- `trie.py` – Implements a Trie data structure for word pattern searches.
- `utils.py` – Utility functions, such as initializing guessed letters.
- `word_loader.py` – Loads words from a file.
 - `filter-ordnet.py` – Filters words based on specific criteria, ensuring they contain at least five unique letters and do not include numbers or unwanted special characters. This script processes an input word list and generates a filtered list along with a separate file for removed words.
 - `game.py` – Implements the interactive Hangman game, including guessing logic, hints, and visual representation.
 
## Future Enhancements
 
- Support for **multi-word Hangman phrases**.
- Additional **heuristics for word guessing**.
 
## License
 
This project is licensed under the **MIT License**. Feel free to modify and distribute it.
 
## Contributions
 
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Submit a pull request.
