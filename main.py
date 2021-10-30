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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def inventory_report():
    for key, value in resources.items():
        print(key, " : ", value)


def check_inventory(drink):
    for key, value in MENU[drink]["ingredients"].items():
        if value > resources[key]:
            print("We don't have enough", str(key), "at the moment, sorry.")
            return "fail"
    return "success"


def handle_money(drink):
    print("Your drink will cost $" + str(MENU[drink]["cost"]) + ".")
    q = int(input("Please input how many quarters you'll use:"))
    d = int(input("Please input how many dimes you'll use:"))
    n = int(input("Please input how many nickels you'll use:"))
    p = int(input("Please input how many pennies you'll use:"))

    total = ((q * 25) + (d * 10) + (n * 5) + (p * 1)) / 100

    if total > MENU[drink]["cost"]:
        print("You gave me $" + str(total) + ", which is too much.")
        print("Here's $" + str(round(total - MENU[drink]["cost"], 2)) + " in change.")
    elif total < MENU[drink]["cost"]:
        print("You gave me $" + str(total) + ", which isn't enough, starting over")
        return "fail"
    resources["money"] += MENU[drink]["cost"]
    return "success"


def make_coffee(drink):
    for key, value in MENU[drink]["ingredients"].items():
        resources[key] -= value


is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "off":
        print("Maintenance mode activated. Machine turning off")
        is_on = False
    elif choice == "report":
        inventory_report()
    else:
        status = check_inventory(choice)
        if status == "success":
            status = handle_money(choice)
            if status == "success":
                make_coffee(choice)
                print("Here is your " + choice + ". Enjoy!")
