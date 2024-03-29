import random


def getTeamOrPlayer() -> list:
    playerOrTeam = ""
    teams = []

    while playerOrTeam not in ["a", "b"]:
        playerOrTeam = input("Will you be playing A) by yourself or B) with 2 teams?").lower()

    if playerOrTeam == "b":
        for team in range(1, 3):
            teamName = ""
            while not teamName.isalpha():
                teamName = input(f"Provide us with a name for team {team}")

    return teams


def checkForTeam(teamlist: list, ifplayer: str, ifteam: str or int) -> str or int:
    if not teamlist:
        return ifplayer
    else:
        return ifteam


def getRandomWord(words: list) -> str:
    chosenWord = ""
    while len(chosenWord) != 5:
        chosenWord = random.choice(words)

    return chosenWord


def filterGuess(guess: str, currentWord: str) -> str:
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Reset = "\u001b[0m"

    splitguess = list(guess)
    splitword = list(currentWord)

    for letter in splitguess:
        amount_of_letters_in_current_word = [i for i in splitword if i == letter]
        amount_of_letters_in_guess = [i for i in list(guess) if i == letter]
        if letter in splitword:
            index = splitguess.index(letter)
            if splitguess[index] == splitword[index]:
                splitguess[index] = Green + letter + Reset
            elif len(amount_of_letters_in_current_word) >= len(amount_of_letters_in_guess) and splitguess[index] != splitword[index]:
                splitguess[index] = Yellow + letter + Reset
            else:
                splitguess[index] = letter + Reset

    return "".join(splitguess)

def playAgain(text: str):
    answer = ""
    while not answer in ["y", "n"]:
        answer = input(text).lower()

    if answer == "n":
        return False

    elif answer == "y":
        return True
