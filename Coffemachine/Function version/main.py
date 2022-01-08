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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_report():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(profit, 'euros')


def process_coins():
    """Returns the total amount from the coins inserted"""
    print('Please insert coins.')
    amount = 0
    amount += int(input('how many quarters?')) * 0.25
    amount += int(input('how many dimes?')) * 0.10
    amount += int(input('how many nickles?')) * 0.05
    amount += int(input('how many pennies?')) * 0.01
    return amount


def is_resource_sufficient(order_ingredients):
    """Return true if the resources are sufficient for making a drink, else it returns false"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'sorry not enough {item}')
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} in change")
        profit += drink_cost
        return True
    else:
        print("not enough money")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


def print_ascii(fn):
    f = open(fn, 'r')
    print(''.join([line for line in f]))


is_on = True

while is_on:
    print_ascii('art.txt')
    choice = input('What do you want to buy? espresso, latte, cappuccino, off - to exit \n')
    if choice == "off":
        is_on = False
    elif choice == 'report':
        get_report()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
