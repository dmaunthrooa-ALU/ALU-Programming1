import random
import requests  # You need this library: pip install requests


def get_random_word():
    """
    Try to get a random word from an online dictionary.
    If the internet is not available, use a local fallback list.
    """
    try:
        # Request one random word with length between 5 and 10 letters
        # (good difficulty for Hangman)
        url = "https://random-word-api.herokuapp.com/word?number=1&length=7"
        response = requests.get(url, timeout=5)  # timeout after 5 seconds

        if response.status_code == 200:
            word = response.json()[0]  # The API returns a list, e.g. ["apple"]
            return word.upper()  # Convert to uppercase for the game
        else:
            print("API returned an error. Using a local word instead.")
    except Exception as e:
        print("Could not connect to the online dictionary.")
        print("Using a local word instead.")

    # Fallback list (used when internet is down or API fails)
    fallback_words = [
        "PYTHON", "COMPUTER", "PROGRAMMING", "HANGMAN",
        "DEVELOPER", "FUNCTION", "VARIABLE", "LOOP",
        "ALGORITHM", "KEYBOARD", "MONITOR", "SOFTWARE"
    ]
    return random.choice(fallback_words)


def display_hangman(tries):
    """Return the hangman drawing that matches the number of remaining tries."""
    stages = [
        # 0 tries left
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # 1 try left
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        # 2 tries left
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        # 3 tries left
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        # 4 tries left
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        # 5 tries left
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        # 6 tries left (start)
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]


def play_one_game(word):
    """
    Play a single game of Hangman with the given secret word.
    Returns True if the player won, False if the player lost.
    """
    word_completion = ['_' for _ in word]  # List of underscores
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("\nLet's play Hangman!")
    print(f"(The word has {len(word)} letters)")
    print(display_hangman(tries))
    print(' '.join(word_completion))
    print()

    while not guessed and tries > 0:
        guess = input("Please guess a letter or the whole word: ").upper()

        # Case 1: Player typed a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                # Reveal every occurrence of the letter
                for i, letter in enumerate(word):
                    if letter == guess:
                        word_completion[i] = guess
                # Check if the word is complete
                if '_' not in word_completion:
                    guessed = True

        # Case 2: Player typed a full word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = list(word)

        # Case 3: Invalid input
        else:
            print("Not a valid guess.")

        # Show current status
        print(display_hangman(tries))
        print(' '.join(word_completion))
        print()

    # End of the round
    if guessed:
        print("Congratulations! You guessed the word!")
        return True
    else:
        print(f"Sorry, you ran out of tries. The word was {word}.")
        return False


def main():
    """Main program – handles multiple games and scoring."""
    wins = 0
    losses = 0

    print("=== Welcome to Hangman (Online Dictionary Version) ===")
    print("Words are fetched from an online dictionary when possible.\n")

    while True:
        # Get a new word (from online dictionary or fallback)
        secret_word = get_random_word()

        # Play one full game
        player_won = play_one_game(secret_word)

        # Update score
        if player_won:
            wins += 1
        else:
            losses += 1

        # Ask if the player wants to continue
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            break

    # Final score
    print("\n========== FINAL SCORE ==========")
    print(f"Wins  : {wins}")
    print(f"Losses: {losses}")
    print("Thanks for playing! Goodbye.")


# Start the game only when the file is run directly
if __name__ == "__main__":
    main()