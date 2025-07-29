# THIS IS MY ROCK PAPER SCISSORS GAME

print("welcome to my game")

player_choice = input("Please select an option ('rock'), ('paper'), ('scissors')")
print("USER CHOSE:", player_choice)

# todo - validation step
 
import random

VALID_OPTIONS = (["rock"],["paper"],["scissors"])

computer_choice = random.choice(VALID_OPTIONS)
print("COMPUTER CHOSE:", player_choice)

if player_choice == computer_choice:
    result = "TIE GAME"
elif player_choice == "rock" and computer_choice == "scissors":
    result = "USER WINS"
elif player_choice == "rock" and computer_choice == "paper":
    result = "COMP WINS"
elif player_choice == "paper" and computer_choice == "rock":
    result = "USER WINS"
elif player_choice == "paper" and computer_choice == "scissors":
    result = "COMP WINS"
elif player_choice == "scissors" and computer_choice == "paper":
    result = "USER WINS"
elif player_choice == "scissors" and computer_choice == "rock":
    result = "COMP WINS"
else:
    result = "INVALID CHOICE"

print(result)

# TODO: determine the winner

print("WINNER: TODO")