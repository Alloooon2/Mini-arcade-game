import random

def rps() -> bool:
    user_wins = 0
    for round in range(3):
        print(f"Round: {round + 1}")
        valid_choices = ["rock", "paper", "scissors"]

        choices = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }

        computer_choice = random.choice(valid_choices)
        user_choice = input("Enter your choice: ")

        while user_choice not in valid_choices:
            print("Invalid choice.")
            user_choice = input("Enter your choice: ")

        print(f"Computer chose: {computer_choice}")

        if choices[user_choice] == computer_choice:
            print("You won!")
            user_wins += 1
        elif user_choice == computer_choice:
            print("Draw")
        else:
            print("Loser")

    return user_wins == 2

scores = []
score = 0

while True:
    print("1. Games")
    print("2. Scoreboard")
    print("3. Quit")

    menu_select = input("Enter your choice (1, 2, 3): ")

    if menu_select == "1":
        while True:
            print("\n1. Hangman")
            print("2. Rock Paper Scissors")
            print("3. Back to menu")

            games = input("Pick a game: ")

            if games == "1":
                print("Hangman")
            elif games == "2":
                if rps():
                    print("You won!")
                    score += 1
                else:
                    print("You lost.")

            elif games == "3":
                scores.append(score)
                score = 0
                break

            else:
                print("Invalid choice")

    elif menu_select == "2":
        if len(scores) == 0:
            print("No scores yet. You can be the first!")
        else:
            print("Top 3 Scores:")
            sorted_scores = sorted(scores, reverse=True)
            for i in range(min(3, len(sorted_scores))):
                print(f"{i + 1}. {sorted_scores[i]}")

    elif menu_select == "3":
        scores.append(score)
        print("Quitting game...")
        break

    else:
        print("Invalid choice")