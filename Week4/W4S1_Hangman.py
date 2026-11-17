import random   # Needed to pick a random word from the word list

# ==========================================================
# FUNCTION 1: Display the current state of the hangman
# ==========================================================
def display_hangman(tries):
    """Return the hangman drawing that matches the number of remaining tries."""
    stages = [  # Index 0 = no tries left (full hangman), index 6 = full lives
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
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
    return stages[tries]   # Return the correct picture

# ==========================================================
# FUNCTION 2: Play one complete round of Hangman
# ==========================================================
def play_one_game(word):
    """Play a single game of Hangman with the given secret word.
    Returns True if the player won, False if the player lost."""

    # Create a list of underscores, one for each letter of the word
    word_completion = ['_' for _ in word]
    guessed = False          # Becomes True when the whole word is guessed
    guessed_letters = []     # Keep track of letters the player has already tried
    guessed_words = []       # Keep track of full-word guesses
    tries = 6                # Player starts with 6 lives

    print("\nLet's play Hangman!")
    print(display_hangman(tries))
    print(' '.join(word_completion))   # Show the current blanks
    print()

    # Main game loop – continues while the player still has lives
    # and has not yet guessed the whole word
    while not guessed and tries > 0:
        guess = input("Please guess a letter or the whole word: ").upper()

        # ----- Case 1: Player typed a single letter -----
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1                 # Lose one life
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                # Reveal every occurrence of the guessed letter
                for i, letter in enumerate(word):
                    if letter == guess:
                        word_completion[i] = guess
                # Check whether the word is now completely revealed
                if '_' not in word_completion:
                    guessed = True

        # ----- Case 2: Player typed a full word -----
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = list(word)   # Reveal the whole word

        # ----- Case 3: Invalid input -----
        else:
            print("Not a valid guess.")

        # Show the updated hangman and the current progress
        print(display_hangman(tries))
        print(' '.join(word_completion))
        print()

    # ----- End of the round -----
    if guessed:
        print("Congratulations! You guessed the word!")
        return True   # Player won
    else:
        print(f"Sorry, you ran out of tries. The word was {word}.")
        return False  # Player lost

# ==========================================================
# FUNCTION 3: Main program – handles multiple games & scoring
# ==========================================================
def main():
    """Entry point of the program. Keeps playing until the user quits
    and keeps track of wins and losses."""

    # A simple list of possible secret words
    word_list = ["PYTHON", "COMPUTER", "PROGRAMMING", "HANGMAN",
                 "DEVELOPER", "FUNCTION", "VARIABLE", "LOOP"]

    wins = 0      # Counter for successful games
    losses = 0    # Counter for lost games

    # Outer loop – keeps offering new games until the player says "no"
    while True:
        # Pick a random word from the list
        secret_word = random.choice(word_list)

        # Play one full game and receive the result (True = win)
        player_won = play_one_game(secret_word)

        # Update the score
        if player_won:
            wins += 1
        else:
            losses += 1

        # Ask the player whether they want another round
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != "Y":
            break   # Exit the while loop

    # Final summary shown only when the player decides to stop
    print("\n========== FINAL SCORE ==========")
    print(f"Wins  : {wins}")
    print(f"Losses: {losses}")
    print("Thanks for playing! Goodbye.")

# ==========================================================
# Start the program only when this file is run directly
# ==========================================================
if __name__ == "__main__":
    main()
