# Define the resources that are available for each type of coffee (for either espresso/latte/cappuccino)

machine_resources = {
    "water": 1000,
    "milk": 2500,
    "coffee": 5000,
}

coffee_types = {
    "latte": {
        "water": 100,
        "milk": 115,
        "coffee": 75,
        "money": 2.50
    },
    "espresso": {
        "water": 100,
        "milk": 150,
        "coffee": 75,
        "money": 3.15
    },
    "cappuccino": {
        "water": 100,
        "milk": 70,
        "coffee": 35,
        "money": 2.99
    }
}

# If user inputs "report" generate a list of the resources needed to make the coffee

def generate_report(coffee_resources):
    print()
    print(f"Water: {coffee_resources["water"]}ml")
    print(f"Milk: {coffee_resources["milk"]}ml")
    print(f"Coffee: {coffee_resources["coffee"]}g")
    print(f"Money: ${coffee_resources["money"]}")
    print()

# Check if resources available in the machine would be enough in order to make the coffee selected

def check_resources(coffee_resources): 

    if coffee_resources["water"] > machine_resources["water"] and coffee_resources["milk"] > machine_resources["milk"] and coffee_resources["coffee"] > machine_resources["coffee"]:

        return [False, "Sorry resources are not enough to make the coffee "]

    elif coffee_resources["water"] > machine_resources["water"]:

        return [False, "Sorry there is not enough water"]
    
    elif coffee_resources["milk"] > machine_resources["milk"]:

        return [False, "Sorry there is not enough milk"]
    
    elif coffee_resources["coffee"] > machine_resources["coffee"]:
        return [False, "Sorry there is not enough coffee"]
    
    else:
        return [True, "Resources are enough!"]


# Ask the user which type of coffee they would like to have

while True:

    user_choice = input(f"What would you like to have? (A: Latte, B: Espresso, C: Cappuccino): ").lower() 

    match user_choice:
        case "a":
            latte_resources = coffee_types["latte"]

            show_resources = input("Show report? (Y or N): ").lower()

            if show_resources == "y":
                generate_report(latte_resources)
            else:
                continue

            availability = check_resources(latte_resources)

            if(availability[0] == True):

                print("")
                
            else:
                print(availability[1])

                continue

        case "b":
            print("You chose Espresso")

        case "c":
            print("You chose Cappuccino")
        
        case _:
            print("Unknown command")
    
    break


# If resources are ok, ask the user to insert coins/money to purchase the coffee


# Calculate the monetary value of the coins inserted into the machine (quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01)


# Is the money enough? Check if the accumulated amount from the coins inserted amounts to the cost of the coffee selected


# If money not enough, "Sorry that's not enough money. Money refunded"


# If money is enough, update the report


# If money inserted is too much, the machine should offer change


# Transaction is successful and there are enough resources to make the drink selected, ingredients should be deducted from the resources available


# If "off" is inputted at any point of the coffee making process, turn off the machine
