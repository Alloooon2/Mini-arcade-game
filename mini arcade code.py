import random
import time


print("1. Games")
time.sleep(1)
print("2. Score")
time.sleep(1)
print("3. Quit")
time.sleep(1)
menu_select = input("Enter your choice (1, 2, 3): ")

while True:
    if menu_select == "1":
        print("1. Rock, paper scissors")
        time.sleep(1)
        print("2. Hangman")
        games = input("Pick a game to play: ")
        if games == "1":
            print("Hangman")
        elif games == "2":
            print("Rock, paper, scissors")
        elif games == "3":
            print("Going back to menu")
        else:
            print("Invalid choice, pick again")
    elif menu_select == "2":
        print("Scoreboard")

    print("monkey time")
