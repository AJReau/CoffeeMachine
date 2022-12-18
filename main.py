# Menu for the coffee machine which includes the resources and price required to make the item
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

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}


# Checks the machine's resources to ensure there is enough milk/water/coffee available
def checkResources(selection):
    for item in selection:
        if selection[item] >= resources[item]:
            print(f"There is not enough {item}")
            return False
    return True


# Calculates the total coins the user has put into the machine
def processCoins():
    print("Please insert coins.")
    total = int(input("How many quarters do you have:")) * 0.25
    total += int(input("How many dimes do you have:")) * .10
    total += int(input("How many nickels do you have:")) * .05
    total += int(input("How many pennies do you have:")) * .01
    return total


# Ensures that enough money has been added to the machine
def isEnoughMoney(cash, drinkCost):
    if cash >= drinkCost:
        change = cash - drinkCost
        change = round(change, 2)
        print(f"Here is your change: ${change}")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# Uses a for loop to remove the resources from the machine based on the drink
def removeResources(drink):
    for item in drink:
        resources[item] -= drink[item]


# Allows entry into the for loop
is_on = True
collectedMoney = 0

while is_on:

    drinkSelection = input("What drink would you like? (espresso/latte/cappuccino)")
    drinkSelection = drinkSelection.lower()

    if drinkSelection == "off":
        is_on = False
    elif drinkSelection == 'report':
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}mL")
        print(f"Money: ${collectedMoney}")
    else:
        drinkSelection = MENU[drinkSelection]
        if checkResources(drinkSelection["ingredients"]):
            payment = processCoins()
            if isEnoughMoney(payment, drinkSelection["cost"]):
                collectedMoney += drinkSelection["cost"]
                removeResources(drinkSelection["ingredients"])
