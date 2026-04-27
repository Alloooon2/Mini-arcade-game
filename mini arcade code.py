import random

# Rock paper scissors game
def rps() -> bool:
    user_wins = 0
    for round in range(3):
        print(f"Round: {round + 1}")
        valid_choices = ["1", "2", "3"]

        choices = { #This is a dictionary which is used here to state what beats what in a less tedious way
            "1": "3",
            "2": "1",
            "3": "2",
        }

        computer_choice = random.choice(valid_choices) # Randomises what the computer picks
        print("1. rock \n2. paper \n3. scissors")
        user_choice = input("Enter your choice (1,2,3): ")

        while user_choice not in valid_choices:
            print("Invalid choice. Please enter either 1,2 or 3.")
            user_choice = input("Enter your choice: ")

        print(f"Computer chose: {computer_choice}")

# Determines whether or not the user wins or loses and adds score
        if choices[user_choice] == computer_choice:
            print("You won!")
            user_wins += 1
        elif user_choice == computer_choice:
            print("Draw")
        else:
            print("Lose")
        print("---------------------------------")

    return user_wins >= 2

#Hangman game

def hangman() -> bool:
    #List of all possible words used in hangman
    valid_words = [
        "cat", "dog", "sun", "hat", "ball", "tree", "book", "fish", "milk", "star",
        "pen", "cup", "car", "bed", "map", "shoe", "cake", "ring", "leaf", "snow",
        "banana", "orange", "purple", "guitar", "pencil", "school", "window", "rocket",
        "butter", "jungle", "planet", "silver", "golden", "flower", "island", "desert",
        "forest", "castle", "dragon", "pirate", "bridge", "camera", "bottle", "basket",
        "awkward", "rhythm", "galaxy", "pneumonia", "xylophone", "mystify", "cryptic",
        "oxygen", "zombie", "wizard", "nightmare", "triangle", "elephant", "dinosaur",
        "computer", "laptop", "keyboard", "software", "hardware", "internet",
        "queue", "jazzy", "fuzzy", "buzzing", "knapsack", "mnemonic", "syndrome",
        "zigzag", "vortex", "blizzard", "jackpot", "jukebox", "buzzkill", "puzzling",
        "pixel", "matrix", "lengthy", "strength", "twelfth", "unknown"
    ]

    random_word = random.choice(valid_words)
    letters_guessed = []
    wrong_letters = []
    lives = 5

    while lives > 0:
        print("Lives:", lives)
        print("Wrong letters: ", wrong_letters)
        print("Word:", " ".join([letter if letter in letters_guessed else "_" for letter in random_word]))
        print("---------------------------------")

        guess = input("Enter your guess: ").lower()

        if len(guess) != 1:
            print("Invalid. Please enter a single letter.")
            continue

        if guess in random_word: # Replaces the '_' with the correct letter if you guessed right
            if guess not in letters_guessed:
                letters_guessed.append(guess)

            if all(letter in letters_guessed for letter in random_word): # Sets condition for winning and breaks loop if condition is met
                print("Word was: ", random_word)
                return True
        else:
            if guess not in wrong_letters:
                print("Wrong Letter.") # Appends the wrong letters into a separate list which is printed at the start of each iteration
                wrong_letters.append(guess)
                lives -= 1
    print("Word was: ", random_word)
    return False

scores = []
score = 0

#The main menu

while True:
    print("1. Games")
    print("2. Scoreboard")
    print("3. Quit")

    menu_select = input("Enter your choice (1, 2, 3): ") #Easier to have the choices just be 1,2,3 as you don't have to worry as much

    if menu_select == "1":
        while True:
            print("1. Hangman")
            print("2. Rock Paper Scissors")
            print("3. Back to menu")

            games = input("Pick a game: ")

            if games == "1":
                if hangman():
                    print("You won Hangman!")
                    score += 1
                else:
                    print("You lost.")

            elif games == "2":
                if rps():
                    print("You won Rock Paper Scissors!")
                    score += 1
                else:
                    print("You lost.")

            elif games == "3":
                if score > 0:
                    scores.append(score)
                score = 0
                break

            else:
                print("Invalid choice")

    elif menu_select == "2":
        if len(scores) == 0:
            print("No scores yet.")
        else:
            print("Top 3 Scores:")
            sorted_scores = sorted(scores,reverse=True) # Reverse sorts the numbers in descending order.
            for i in range(min(3, len(sorted_scores))): # Only prints the top 3 scores recorded
                print(f"{i + 1}. {sorted_scores[i]}")
            print("---------------------------------")

    elif menu_select == "3":
        scores.append(score)
        print("Quitting game.")
        break

    else:
        print("Invalid choice")