import random

options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

def totalWins():
    print(f"Computer won {computer_wins} and you won {user_wins}")
    quit()

def getUserChoice():
    global user_wins, computer_wins
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    while user_choice not in options:
        if user_choice == "q" or user_choice == "quit":
            totalWins()
        else:
            user_choice = input("Invalid choice! Enter rock, paper, scissors, or Q to quit: ").lower()

    if user_choice == computer_choice:
        print("It's a tie")

    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lost. Paper covers Rock.")
            computer_wins += 1
        else:
            print("You win. Rock crushes Scissors")
            user_wins += 1

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win. Paper covers Rock.")
            user_wins += 1
        else:
            print("You lost. Scissors cuts paper")
            computer_wins += 1

    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lost. Rock crushes scissors.")
            computer_wins += 1
        else:
            print("You win. Scissors cuts paper")
            user_wins += 1

    print(f"You chose {user_choice} and the computer chose {computer_choice}")

while True:
    computer_choice = random.choice(options)
    getUserChoice()
