from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

cappuccino = MenuItem
cappuccino.name = "cappuccino"
cappuccino.ingredients = {"water": 250, "milk": 100, "coffee": 24}
cappuccino.cost = 3

latte = MenuItem
latte.name = "latte"
latte.ingredients = {"water": 200, "milk": 150, "coffee": 24}
latte.cost = 2.5

espresso = MenuItem
espresso.name = "espresso"
espresso.ingredients = {"water": 50, "milk": 0, "coffee": 18}
espresso.cost = 1.5

machine_on = True
while machine_on:
    options = menu.get_items()
    user_selection = input(f"What would you like? ({options}): ").lower()

    if user_selection == "report":
        coffee_machine.report()
        money_machine.report()
    elif user_selection == "off":
        machine_on = False
        print("Powering off.")
    elif user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":
        drink = menu.find_drink(user_selection)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
    else:
        print("Invalid selection. Please try again.")
