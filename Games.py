# Random numbers
# import random
# number=random.randint(1,10)
# print(number)

# options=("Paper","Eraser","Rock","Sticker","Scissor")
# option=random.choice(options)
# print(option)

# cards=["2","3","4","5","6","7","8","9","J","Q","K","A"]
# random.shuffle(cards)
# print(cards)

# Rock Paper Scissors Game
# import random 
# options=("rock","paper","scissors")
# running=True

# while running:
#     player=None
#     computer=random.choice(options)
#     while player not in options:
#         player=input("Enter a choice (rock, paper, scissors): ")
#         print(f"Player: {player}")
#         print(f"Computer: {computer}")

#         if player == computer:
#             print("It's a tie!")
#         elif player == "rock" and computer == "scissors":
#             print("You win!")
#         elif player == "paper" and computer == "rock":
#             print("You win!")
#         elif player == "scissors" and computer == "paper":
#             print("You win!")
#         else:
#             print("You lose!")
#         if not input("Play again? (y/n): ").lower() == "y":
#             running=False 
# print("Thanks for playing!")

# Python Number Guessing Game

# import random 
# lowest_num=1
# highest_num=100
# answer=random.randint(lowest_num,highest_num)
# guesses=0
# is_running=True
# print("Number Guessing Game")
# print(f"Select a number b/w {lowest_num} and {highest_num}")

# while is_running:
#     guess=input("Enter your guess: ")
#     if guess.isdigit():
#         guess=int(guess)
#         guesses+=1
#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number b/w {lowest_num} and {highest_num}")
#         elif guess<answer:
#             print("Too low! Try again!")
#         elif guess>answer:
#             print("Too high! Try again!")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running=False
#     else:
#         print("Invalid guess!")
#         print(f"Please select a number b/w {lowest_num} and {highest_num}")


# Dice program

import random 
# print("\u25CF \u250c \u2500 \u2510 \u2502 \u2514 \u2518")(• ┌ ─ ┐ │ └ ┘)

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art={
    1: ("┌─────────┐",
        "│         │",
        "│    •    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ •       │",
        "│         │",
        "│      •  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ •       │",
        "│   •    │",
        "│      •  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ •     • │",
        "│         │",
        "│ •     • │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ •     • │",
        "│    •    │",
        "│ •     • │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ •    •  │",
        "│ •    •  │",
        "│ •    •  │",
        "└─────────┘")
}

dice=[]
total=0
num_of_dice=int(input("How many dice?: "))
for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end=" ")
    print()

for die in dice:
    total+=die
print(f"Total: {total}")