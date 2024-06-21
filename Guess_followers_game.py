#import libraries
from art import logo, vs
import random
from game_data import data
from replit import clear

score = 0
continue_game = True
item2 = random.choice(data)

    # Declare all the functions
    # Checks which is correct
def answer():
    if item1['follower_count'] > item2['follower_count']:
        return "A"
    else:
        return "B"

# Checks user input to calculated answer
def check_answer(guess, answer):
    global score
    if guess == answer():
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}")

# Formats the data
def format_account(data):
    """Format the account data into a printable format."""
    info = f"{data['name']}, a {data['description']}, from {data['country']}"
    return info


while continue_game:
    item1 = item2
    item2 = random.choice(data)

    while item1 == item2:
        item2 = random.choice(data)

    clear()
    print(logo)

    print(f"Compare A: {format_account(item1)}")
    print(vs)
    print(f"Against B: {format_account(item2)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    check_answer(guess, answer)
