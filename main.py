MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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
ans=True
money=0
sum_money=0

def espresso():
    global MENU,resources,money

    resources["water"]-=50
    resources["coffee"]-=18
    money+=1.5
    print("Here is your espresso☕.Enjoy!")


def latte():
    global MENU,resources,money

    resources["water"]-=200
    resources["coffee"]-=24
    resources['milk']-=150
    money+=2.5
    print("Here is your latte☕.Enjoy!")

def cappuccino():
    global MENU,resources,money

    resources["water"]-=250
    resources["coffee"]-=24
    resources['milk']-=100
    money+=3.0
    print("Here is your cappuccino☕.Enjoy!")

def report():
    global resources,money
    print(f"Water:{resources['water']}")
    print(f"Milk:{resources['milk']}")
    print(f"Coffee:{resources['coffee']}")
    print(f"Money:${money}")

def game():
    global ans,MENU,resources,sum_money
    while ans:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == 'report':
            report()

        elif user_choice in MENU:
            quarters = float(input("Please insert coins.\nHow many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))

            sum_money = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)

            if resources["water"] < MENU[user_choice]["ingredients"]["water"]:
                print("Sorry there is not enough water.")
                game()

            if resources["water"] < MENU[user_choice]["ingredients"]["coffee"]:
                print("Sorry there is not enough water.")
                game()

            if resources["milk"] < MENU[user_choice]["ingredients"]["milk"]:
                print("Sorry there is not enough water.")
                game()

            if sum_money < MENU[user_choice]['cost']:
                print("Sorry that's not enough money. Money refunded.")
                game()

            elif sum_money > MENU[user_choice]['cost']:
                change = round((sum_money - 1.5), 2)
                print(f"Here is ${change} in change.\n")

            if user_choice == 'espresso':
                espresso()
            elif user_choice == 'latte':
                latte()
            elif user_choice == 'cappuccino':
                cappuccino()




        elif user_choice == 'off':
            ans = False
            break
        else:
            print("Invalid input.TRY AGAIN!")

game()






