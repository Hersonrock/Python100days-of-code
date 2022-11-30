from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on= True
coffe_machine=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()


# choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
# if choice=="report":
#     coffe_machine.report()
#     money_machine.report()
# elif choice=="espresso" or choice== "latte" or choice =="cappuccino":

while is_on:

    options= menu.get_items()
    choice=input(f"What would you like? ({options}): ").lower()
    if choice=="report":
        coffe_machine.report()
        money_machine.report()
    elif choice=="off":
        is_on =False
    else:
         drink=menu.find_drink(choice)
         if coffe_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_machine.make_coffee(drink)

print("Good Bye...")