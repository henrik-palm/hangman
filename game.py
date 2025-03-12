import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def get_hangman_art(attempts):
    stages = [
        """
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        """
          +---+
              |
              |
              |
              |
              |
        =========
        """,
        """

              |
              |
              |
              |
              |
        =========
        """,
        """

              
              
              
              
              
        =========
        """
    ]
    return stages[attempts]

def hangman(word=None):
    clear_screen()
    if word is None:
        word = input("Enter the word for Hangman: ").strip().lower()
    clear_screen()
    guessed_letters = set()
    attempts = 9
    last_message = "Welcome to Hangman!"

    while attempts > 0:
        clear_screen()
        print(get_hangman_art(attempts))
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Wrong attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else ''}")
        if last_message:
            print(last_message)
        
        guess = input("Enter a letter: ").strip().lower()
        
        if len(guess) != 1 or not guess.isalpha():
            last_message = "Invalid input. Please enter a single letter."
            continue

        if guess in guessed_letters:
            last_message = f"You've already guessed {guess}."
            continue

        guessed_letters.add(guess)
        
        if guess not in word:
            attempts -= 1
            last_message = f"Incorrect! {guess} is not in the word."
        else:
            last_message = f"Good guess! {guess} is in the word."

        if all(letter in guessed_letters for letter in word):
            clear_screen()
            print(get_hangman_art(attempts))
            print(f"Word: {display_word(word, guessed_letters)}")
            print(f"Attempts left: {attempts}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        clear_screen()
        print(get_hangman_art(attempts))
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()