print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input()# What is their name?

names = (name1 + name2).lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

digit_1 = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

digit_2 = l + o + v + e

score = int(str(digit_1) + str(digit_2))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
