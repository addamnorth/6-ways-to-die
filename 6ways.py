import random
import time

# define the options
options = ["rock", "paper", "scissors", "lizard", "spock", "fire", "water"]

# define the rules
rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"],
    "fire": ["scissors", "paper", "lizard"],
    "water": ["rock", "fire", "scissors"]
}

# define the art for each option
art = {
    "rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """,
    "lizard": """
         _______
    ---'    ____)_
               (_____)
            ____(____)
           (____)
    ---.__(___)
    """,
    "spock": """
         _______
    ---'    ____)_
               (_____)
            ____(____)
           (____)
    ---.__(___)
    """,
    "fire": """
          /\_
         (    )
        (      )
    \  \----/  /
     \        /
      \  __  /
    """
    ,
    "water": """
          /\_
         (    )
        (      )
    \  /----\  /
     \/      \/
    """
}

# initialize scores
player_score = 0
computer_score = 0

# define function to print game options
def print_options():
    print("\n".join([f"{i+1}. {option.title()}" for i, option in enumerate(options)]))

# game loop
while True:
    # print current scores
    print("\n")
    print(f"{'PLAYER':<10}{'COMPUTER':<10}")
    print(f"{player_score:<10}{computer_score:<10}")
    print("-" * 20)

    # print game options
    print("Select your move:")
    print_options()

    # get player input
    player_choice = input("> ").lower()

    # check for valid input
    if player_choice not in options:
        print("Invalid input. Try again.")
        continue

    # get computer input
    print("Computer is thinking...")
    time.sleep(1)
    computer_choice = random.choice(options)

    # print choices
    print("\n")
    print(f"You chose: {player_choice.title()}")
    print("".join([f"{line}\n" for line in art[player_choice]]))
    print(f"Computer chose: {computer_choice.title()}")
    print("".join([f"{line}\n" for line in art[computer_choice]]))

    # determine winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif computer_choice in rules[player_choice]:
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score
