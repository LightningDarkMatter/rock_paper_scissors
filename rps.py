import random

options = ["rock", "paper", "scissors"]

computer = random.choice(options)

player = input("Choose rock, paper, or scissors: ")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "paper":
        print("You lose!", computer, "covers", player)
    else:
        print("You win!", player, "smashes", computer)
elif player == "paper":
    if computer == "scissors":
        print("You lose!", computer, "cut", player)
    else:
        print("You win!", player, "covers", computer)
elif player == "scissors":
    if computer == "rock":
        print("You lose...", computer, "smashes", player)
    else:
        print("You win!", player, "cut", computer)
else:
    print("That's not a valid choice.")
