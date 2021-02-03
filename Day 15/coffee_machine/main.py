# Dictionary containing drinks information
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

# Dictionary containing machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report():
    """Prints a report of the status of machine's resources"""

    # Retrieves the amount of water
    water = resources["water"]

    # Retrieves the amount of milk
    milk = resources["milk"]

    # Retrieves the amount of coffee
    coffee = resources["coffee"]

    # Retrieves the amount of money
    money = resources["money"]

    # Returns the machine's resources report
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"


def check_resources(drink):
    """Checks if machine's resources are sufficient to make the drink"""

    # Goes through all ingredients needed to make the drink
    for item in MENU[drink]["ingredients"]:
        # Checks if there is an ingredient for which resources are not sufficient
        if resources[item] < MENU[drink]["ingredients"][item]:
            # Prints a message to the user indicating that there is not enough of current ingredient to make the drink
            print(f"Sorry there is not enough {item}.")

            # Returns False as there is at least one resource missing
            return False

    # Returns True as there is enough resources to make the drink
    return True


def refresh_resources(drink):
    """Refresh machine's resources after a drink has been served"""

    # Adds the cost of the drink to the amount of money
    resources["money"] += MENU[drink]["cost"]

    # Goes through all ingredients needed to make the drink
    for item in MENU[drink]["ingredients"]:
        # Subtracts the quantity of the current ingredient to the machine's resources
        resources[item] -= MENU[drink]["ingredients"][item]


def check_money(drink):
    """Prompts the user to insert coins and checks if he inserted enough"""

    # Prompts the user to insert coins
    print("Please insert coins.")

    # Stores the user input for quarters
    quarters = int(input("how many quarters?: "))

    # Stores the user input for dimes
    dimes = int(input("how many dimes?: "))

    # Stores the user input for nickels
    nickels = int(input("how many nickels?: "))

    # Stores the user input for pennies
    pennies = int(input("how many pennies?:"))

    # Retrieves the cost of the drink the user chose
    cost = MENU[drink]["cost"]

    # Computes the total money inserted by the user
    money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    # Checks if the user inserted enough money
    if money >= cost:
        # The user inserted enough money

        # Refreshes the machine's resources
        refresh_resources(drink)

        # Computes the change
        change = round(money - cost, 2)

        # Returns the amount of change as a string
        return f"Here is ${change} in change.\nHere is your {drink} ☕️. Enjoy!"
    else:
        # The user didn't insert enough money

        # Returns a message to the user indicating he didn't inserted enough money
        return "Sorry that's not enough money. Money refunded."


def coffee_machine():
    """Starts the coffee machine and makes it run"""

    # Initializes the variable indicating if the machine goes off
    off = False

    # As long as the machine is not off, it runs
    while not off:
        # Stores user's machine choice
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Tests the user's choice
        if user_choice == "off":
            # The user is a technician and turned off the machine using the choice "off"

            # The variable off becomes True which will stop the machine
            off = True
        elif user_choice == "report":
            # The user asked for a report of the machine's resources using the choice "report"

            # Prints the machine's report
            print(report())
        elif user_choice in MENU:
            # The user asked for a drink among "espresso", "latte" or "cappuccino"

            # Checks if the machine has sufficient resources to make the drink
            if check_resources(user_choice):
                # The machine has sufficient resources

                # Asks the user to insert coins and checks if the user inserted enough to pay the drink
                print(check_money(user_choice))
        else:
            # The user made an invalid choice

            # Prints the user he made an invalid choice
            print("Invalid choice")


# Starts the coffee_machine
coffee_machine()
