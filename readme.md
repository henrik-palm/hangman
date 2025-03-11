

# Hangman Solver
 
This is a **Hangman solver** implemented in Python. It uses **trie-based word searching** and **letter frequency analysis** to determine the best strategy for guessing words in a game of Hangman. The solver can evaluate a batch of words in parallel and determine whether a winning strategy exists for each word.
 
## Features
 
- **Efficient Trie-based word lookup** to quickly find words matching a pattern.
- **Letter frequency analysis** to determine the most optimal guesses.
- **Parallel processing support** to handle large word lists efficiently.
- **Customizable maximum wrong guesses** to simulate different difficulty levels.
- **Verbose mode** for debugging and detailed output.
 
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
 
## Future Enhancements
 
- Support for **multi-word Hangman phrases**.
- Additional **heuristics for word guessing**.
- Integration with an **interactive Hangman game interface**.
 
## License
 
This project is licensed under the **MIT License**. Feel free to modify and distribute it.
 
## Contributions
 
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Submit a pull request.
