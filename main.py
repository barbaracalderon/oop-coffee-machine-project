from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

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