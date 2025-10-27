coffee = {
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

coffee_types = list(coffee.keys())

print(coffee["espresso"]["water"])
print(type(coffee_types))