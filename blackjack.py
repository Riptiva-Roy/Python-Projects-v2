from art import logo
import random
from replit import clear

print(logo)

def result():
  if user_score > 21:
    print("You went over. You lose 😤")
  elif user_score == 21:
    print("You win with a Blackjack 😎")
  elif user_score == computer_score:
    print("Draw 🙃")
  elif user_score > computer_score:
    print("You win 😃")
  elif user_score < computer_score:
    print("You lose 😤")
  
  
  
game = input("Do you want to play a game of Blackjack? Type 'y'or 'n': ")

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

user_cards = random.choices(cards, k=2)
user_score1 = user_cards[0] + user_cards[1]

print(f"Your cards: {user_cards}, current score:{user_score1}") 

computer_cards = random.choices(cards, k=2)
computer_score = computer_cards[0] + computer_cards[1]
if computer_score < 17:
  computer_cards.append(random.choice(cards))
  computer_score = computer_cards[0] + computer_cards[1] + computer_cards[2]

print(f"Computer's first card: {computer_cards[0]}")


if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
  user_cards.append(random.choice(cards))
  user_score = user_cards[0] + user_cards[1] + user_cards[2]
  result()
else:
  print("Computer's final hand: {computer_hand}, final score: {computer_score}")
  result()
