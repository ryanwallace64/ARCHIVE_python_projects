MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = float(0)

def power_off():
    '''Power machine off'''
    print("Powering off.")
    return False

def report():
    '''Print report of available resources'''
    print(resources["water"])
    print(resources["milk"])
    print(resources["coffee"])
    print(f"${money}")

def check_resources(selection):
    '''Check to ensure enough of each resource prior to taking customer's money'''
    if resources["water"] < MENU[selection]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
        return 0
    if resources["milk"] < MENU[selection]["ingredients"]["milk"]:
        print("Sorry, there is not enough milk.")
        return 0
    if resources["coffee"] < MENU[selection]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
        return 0

def take_money(selection):
    global money
    print(f"Please enter ${MENU[selection]['cost']}.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    total = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)

    if total < MENU[selection]['cost']:
        print("Sorry, that's not enough. Money refunded")
        return 0
    else:
        money += MENU[selection]['cost']
        if total > MENU[selection]['cost']:
            print(f"Here is ${round(total - MENU[selection]['cost'], 2)} in change.")


def brew(selection):
    '''Brew user selection if resources and change are sufficient'''
    if check_resources(selection) == 0:
        return

    if take_money(selection) == 0:
        return

    resources["water"] -= MENU[selection]["ingredients"]["water"]
    resources["milk"] -= MENU[selection]["ingredients"]["milk"]
    resources["coffee"] -= MENU[selection]["ingredients"]["coffee"]

    print(f"Please take your {selection}. Thank you!")



machine_on = True
while machine_on:
    user_selection = input("What would you like? 'espresso', 'latte', or 'cappuccino': ").lower()

    if user_selection == "off":
        machine_on = power_off()
    elif user_selection == "report":
        report()
    elif user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":
        brew(user_selection)
    else:
        print("You have entered an invalid selection. Please try again.")