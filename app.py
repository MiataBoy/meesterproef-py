from functions import *
from words import words

# Vital variables for gameplay:
gameplay = True
guesses = 1
failedguesses = {}
replay = "Waiting"

print("Starting Lingo EN...")

currentWord = getRandomWord(words)
user = getTeamOrPlayer()
maxguesses = 5 if not user else 10

while gameplay:
    if failedguesses:
        print(f"Previous guess{' by team ' + user[1] if user else ''}: {failedguesses[guesses - 1]}")
    else:
        print(f"The word starts with letter {currentWord[0]}")

    guess = ""
    while not len(guess) == 5 or guess.isalpha():
        guess = input(f"Guess {guesses}{' for team ' + user[0] if user else ''}. Please provide a guess of 5 letters or type stop to stop.")
        if guess == "stop":
            guesses = maxguesses
            guess = "stop!"

    if guess == currentWord:
        replay = playAgain(
            f"{'Team ' + user[0] if user else 'You'} guessed {currentWord} correctly, congrats! You took {guesses} guesses.\nDo you want to play again? Y/N")

        if replay:
            guesses = 1
            failedguesses = {}
            print("Restarting Lingo EN...")
            currentWord = getRandomWord(words)
            maxguesses = 5 if not user else 10
        else:
            gameplay = False

    if guesses == maxguesses:
        replay = playAgain(f"Unfortunately you did not guess {currentWord}. Want to give it another try? Y/N")
        if replay:
            guesses = 1
            failedguesses = {}
            print("Restarting Lingo EN...")
            currentWord = getRandomWord(words)
            maxguesses = 5 if not user else 10
        else:
            gameplay = False


    elif guess != currentWord:
        guess = filterGuess(guess, currentWord)

        failedguesses[guesses] = guess
        guesses += 1
        if user:
            user.reverse()
