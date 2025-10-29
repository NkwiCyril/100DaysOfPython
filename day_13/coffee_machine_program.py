# Define the resources that are available for each type of coffee (for either espresso/latte/cappuccino)

machine_resources = {
    "water": 100,
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
    
    show_resources = input("Show report? (Y or N): ").lower()

    print()

    if show_resources == "y":
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

# Calculate the monetary value of the coins inserted into the machine (quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01)

def calculate_monetary_value(to_be_paid):

    print("Time to pay!")

    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    total_amount = sum([(quarters * 0.25), (dimes * 0.10), (nickels * 0.05), (pennies * 0.01)])

    print()

    print(f"TOTAL AMOUNT: ${round(total_amount, 2)}")

    if total_amount < to_be_paid:
        print("Sorry that's not enough money. Money refunded")

        return [False, "Money not enough"]

    else:

        change = total_amount - to_be_paid

        return [change, "Money is more than amount"]


# Transaction is successful and there are enough resources to make the drink selected, ingredients should be deducted from the resources available

def update_resources(coffee_type, coffee_resources):
    machine_resources["water"] -= coffee_resources["water"]
    machine_resources["milk"] -= coffee_resources["milk"]
    machine_resources["coffee"] -= coffee_resources["coffee"]
    
    print(f"MACHINE RESOURCES: {machine_resources}")
    
def enjoy_your(coffee_type):
    print(f"Here is your {coffee_type}. Enjoy!")

# Ask the user which type of coffee they would like to have

while True:

    change = 0.00

    print()

    user_choice = input(f"What would you like to have? (A: Latte, B: Espresso, C: Cappuccino): ").lower() 

    match user_choice:
        case "a":
            latte_resources = coffee_types["latte"]

            generate_report(latte_resources)

            availability = check_resources(latte_resources)

            if(availability[0] == True):
                
                money_calculation = calculate_monetary_value(latte_resources["money"])

                if money_calculation[0] == False:
                    continue
                else:
                    change = round(money_calculation[0], 2)

                    print(money_calculation[1])
                    print(f"Your change is ${change}")
                
                update_resources("latte", latte_resources)
                
                generate_report(latte_resources)

                enjoy_your("latte")
                    
            else:
                print(availability[1])

                continue

        case "b":
            espresso_resources = coffee_types["espresso"]

            generate_report(espresso_resources)

            availability = check_resources(espresso_resources)

            if(availability[0] == True):
                
                money_calculation = calculate_monetary_value(espresso_resources["money"])

                if money_calculation[0] == False:
                    continue
                else:
                    change = round(money_calculation[0], 2)

                    print(money_calculation[1])
                    print(f"Your change is ${change}")
                
                update_resources("espresso", espresso_resources)
                
                generate_report(espresso_resources)

                enjoy_your("espresso")
                    
            else:
                print(availability[1])

                continue

        case "c":
            cappuccino_resources = coffee_types["cappuccino"]

            generate_report(cappuccino_resources)

            availability = check_resources(cappuccino_resources)

            if(availability[0] == True):
                
                money_calculation = calculate_monetary_value(cappuccino_resources["money"])

                if money_calculation[0] == False:
                    continue
                else:
                    change = round(money_calculation[0], 2)

                    print(money_calculation[1])
                    print(f"Your change is ${change}")
                
                update_resources("cappuccino", cappuccino_resources)
                
                generate_report(cappuccino_resources)

                enjoy_your("cappuccino")
                    
            else:
                print(availability[1])

                continue
        
        case _:
            print("Unknown command")
