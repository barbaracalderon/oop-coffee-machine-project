from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = MoneyMachine()


user_choice = str(input(f'Welcome to the Coffee Machine!\nWhat would you like? ({menu.get_items()}): '))
if user_choice == 'report':
    machine.report()
elif menu.find_drink(user_choice) is not None:
    menu_item = MenuItem(user_choice)
    machine.process_coins()
    machine.make_payment(menu_item.cost)