print("Welcome to the Adventure Game!")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose? \n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
elif choice1 == "right":
    choice2 = input('You\'ve come to a forest. There is a path that splits into two. Type "left" to take the left path or "right" to take the right path. \n').lower()
    if choice2 == "left":
        choice3 = input('You encounter a friendly wizard. He offers you a choice of two potions: one red and one green. Which one do you choose? Type "red" or "green". \n').lower()
        if choice3 == "red":
            print("The potion gives you super strength. You easily defeat any challenges ahead and find the treasure. You Win!")
        elif choice3 == "green":
            print("The potion makes you invisible, but you accidentally walk off a cliff. Game Over.")
        else:
            print("You chose an option that doesn't exist. Game Over.")
    elif choice2 == "right":
        choice3 = input('You encounter a sleeping dragon. Do you "sneak" past it or "fight" it? \n').lower()
        if choice3 == "sneak":
            choice4 = input("You successfully sneak past the dragon and find two chests. Do you open the 'gold' chest or the 'silver' chest? \n").lower()
            if choice4 == "gold":
                print("The chest is filled with gold coins. You Win!")
            elif choice4 == "silver":
                print("The chest contains a trap and you are caught. Game Over.")
            else:
                print("You chose an option that doesn't exist. Game Over.")
        elif choice3 == "fight":
            choice4 = input("The dragon wakes up and you have to decide quickly. Do you use a 'sword' or 'magic'? \n").lower()
            if choice4 == "sword":
                print("The dragon is too strong and you are defeated. Game Over.")
            elif choice4 == "magic":
                print("Your magic spell works and the dragon is defeated. You find the treasure behind it. You Win!")
            else:
                print("You chose an option that doesn't exist. Game Over.")
        else:
            print("You chose an option that doesn't exist. Game Over.")
    else:
        print("You chose a path that doesn't exist. Game Over.")
else:
    choice2 = input('You\'ve entered a dark cave. Do you want to "explore" further or "exit" the cave? \n').lower()
    if choice2 == "explore":
        choice3 = input('You find a hidden passage. Do you want to go "inside" or keep "walking" in the cave? \n').lower()
        if choice3 == "inside":
            choice4 = input("Inside, you find a room with a sleeping guard. Do you 'sneak' past or 'attack' the guard? \n").lower()
            if choice4 == "sneak":
                print("You successfully sneak past and find the treasure. You Win!")
            elif choice4 == "attack":
                print("The guard wakes up and captures you. Game Over.")
            else:
                print("You chose an option that doesn't exist. Game Over.")
        elif choice3 == "walking":
            print("You get lost in the cave and never find your way out. Game Over.")
        else:
            print("You chose an option that doesn't exist. Game Over.")
    elif choice2 == "exit":
        print("You safely exit the cave and find your way back home. Game Over.")
    else:
        print("You chose an option that doesn't exist. Game Over.")
