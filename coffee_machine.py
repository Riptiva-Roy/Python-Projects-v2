# Define the menu with ingredients and costs
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initial resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Initial money
money = 0

# Function to process inserted coins
def money_processing():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    user_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return user_money

# Function to check if resources are sufficient
def resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# Function to check if the user has inserted enough money
def money_checking(user_money, drink_price):
    global money
    if user_money < drink_price:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(user_money - drink_price, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        money += drink_price
        return True

# Function to make coffee and deduct resources
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

# Function to generate a report of resources and money
def generate_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# Main loop to run the coffee machine
is_on = True

while is_on:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "off":
        is_on = False
    elif drink == "report":
        generate_report()
    elif drink in MENU:
        drink_ingredients = MENU[drink]["ingredients"]  # This is where order_ingredients is defined
        drink_price = MENU[drink]["cost"]

        if resources_sufficient(drink_ingredients):
            user_money = money_processing()
            if money_checking(user_money, drink_price):
                make_coffee(drink, drink_ingredients)
    else:
        print("Invalid choice. Please select from espresso, latte, or cappuccino.")
