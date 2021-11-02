from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
register = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}):")

    if choice == "off":
        print("Maintenance mode activated. Turning machine off.")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        register.report()
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            print("Please make a valid selection")
        else:
            can_make = coffee_maker.is_resource_sufficient(drink)
            if can_make is True:
                made_payment = register.make_payment(drink.cost)
                if made_payment is True:
                    coffee_maker.make_coffee(drink)
