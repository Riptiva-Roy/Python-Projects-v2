from art import logo
import random
print(logo)

print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

numbers = []
for i in range(1,101):
  numbers.append(i)

answer = random.choice(numbers)

if level == "easy":
  attempts = 10
  while attempts > 0:
    guess = int(input("Make a guess: "))
    attempts -= 1
    if guess == answer:
      print(f"You got it! The answer was {answer}.")
      attempts = 0
    elif guess > answer:
      print("Too high.")
      print(f"You have {attempts} attempts remaining to guess the number.")  
    else:
      print("Too low")
      print(f"You have {attempts} attempts remaining to guess the number.")

elif level == "hard":
  attempts = 5  
  while attempts > 0:
    guess = int(input("Make a guess: "))
    attempts -= 1
    if guess == answer:
      print(f"You got it! The answer was {answer}.")
      attempts = 0
    elif guess > answer:
      print("Too high.")
      print(f"You have {attempts} attempts remaining to guess the number.")  
    else:
      print("Too low")
      print(f"You have {attempts} attempts remaining to guess the number.")



