from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    """Starts the coffee machine and makes it run"""

    # Creates a new CoffeeMaker object
    coffee_maker = CoffeeMaker()

    # Creates a new MoneyMachine object
    money_machine = MoneyMachine()

    # Creates a new Menu object
    menu = Menu()

    # Initializes the variable indicating if the machine goes off
    off = False

    # As long as the machine is not off, it runs
    while not off:
        # Displays the machine's menu to the user and stores his choice
        user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()

        # Checks the user's choice
        if user_choice == "off":
            # The user is a technician and turned off the machine using the choice "off"

            # The variable off becomes True which will stop the machine
            off = True
        elif user_choice == "report":
            # The user asked for a report of the machine's resources using the choice "report"

            # Prints the coffee maker report
            coffee_maker.report()

            # Prints the money machine report
            money_machine.report()
        else:
            # Looks for the user's choice in the menu
            drink = menu.find_drink(user_choice)

            # Checks if the user selected an existing drink
            if drink != "None":
                # The user asked for a drink among the menu

                # Checks if the machine has sufficient resources to make the drink
                if coffee_maker.is_resource_sufficient(drink):
                    # The machine has sufficient resources

                    # Asks the user to insert coins and checks if the user inserted enough to pay the drink
                    money_machine.make_payment(drink.cost)

                    # Deducts ingredients of the drink from the machine's resources
                    coffee_maker.make_coffee(drink)
            else:
                # The user made an invalid choice

                # Prints the user he made an invalid choice
                print("Invalid choice")


# Starts the coffee_machine
coffee_machine()
