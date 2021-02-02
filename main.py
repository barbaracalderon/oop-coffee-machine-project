from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print('''\033[33m
         )))
        (((
      +-----+
      |     |] - WELCOME TO THE COFFEE MACHINE!
      `-----' 

      ------ MENU ------ 
      Espresso ($1.50)
      Latte ($2.50)
      Cappuccino ($3.00)
      ------------------

      PS: Type "report" at any moment
      to check our resources available.
      Type "off" to log out from the machine.\033[m
    ''')


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    options = menu.get_items()
    user_choice = str(input(f'What would you like?\nOptions ({options}): ')).strip().lower()
    if user_choice == 'off':
        print('\033[31m<<THE END>>\033[m')
        is_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_choice) is None:
        print('\033[31mError. Please choose an available option.\033[m')
