from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def test ():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money = MoneyMachine()

    options = menu.get_items()



    while True:
        user_input = input(f"What would you like? {options} ? : ")

        if user_input == "report":
            print(f"{coffee_maker.report()} \n {money.report()}")

        elif user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":

            drink = menu.find_drink(user_input)
            enough_resources = coffee_maker.is_resource_sufficient(drink)

            if enough_resources and money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

        elif user_input == "off":
            break

        else:
            print("Please enter from one of the option")


def final():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    is_on = True

    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

test()
# get the name of the drink
# check if enought resources
# get payment
# make coffee


# user_payment = money.make_payment()
