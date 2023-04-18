from menu import MENU
from coffee_resources import resources

profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry rhere is not enough {item}.')
            return False
    return True

def process_coins():
    print('Please insert coins')
    total = int(input('how many quarters?: ')) * 0.25
    total += int(input('how many dimes?: ')) * 0.1
    total += int(input('how many nickles?: ')) * 0.05
    total += int(input('how many pennies?: ')) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry that`s not enough money. Money refounded')

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕️. Enjoy!')

is_on = True

while is_on:
    choise = input('What would you like? (espresso/latte/cappuccino): ')
    if choise == 'off':
        is_on = False
    elif choise == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choise]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choise, drink['ingredients'])
