import random
import sys
from termcolor import colored


def read_random_word():
    with open("sgb-words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)


def print_menu():
    print("Let's play wordle! Type a 5 letter word and hit enter.")


def guessing():
    attempt = 0
    word = read_random_word()
    while attempt < 6:
        guess = input().lower()
        if len(guess) != 5:
            print("Guess must be 5 letters")
            continue

        colored_guess = ""
        for i in range(5):
            if guess[i] == word[i]:
                colored_guess += colored(guess[i], "green")

            elif guess[i] in word:
                colored_guess += colored(guess[i], "yellow")

            else:
                colored_guess += colored(guess[i], "red")

        guessHistory.append(colored_guess)

        for g in guessHistory:
            print(g)

        if guess == word:
            if attempt == 0:
                print(f"\nCongrats! You got the wordle on the first try! Pure luck?")
            else:
                print(f"\nCongrats! You got the wordle in {attempt+1} tries!")
            break

        attempt += 1
        print("\n")

    else:
        print(f"\nYou did not guess the right word. The word was {word}")


print_menu()
word = read_random_word()
guessHistory = []

while True:
    guessing()
    typed = input("Press Enter to keep playing or type 'stop' to exit: ")

    if typed.lower() == "stop":
        print("\n\nThanks for playing!")
        break

    print("Let's play again!")
