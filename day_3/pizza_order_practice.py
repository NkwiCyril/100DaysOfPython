print("Welcome to Python Pizza Deliveries!") 

size = input("What size do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N?: ").lower()

final_amount = 0

if size == "s":
    final_amount += 15
elif size == "m":
    final_amount += 20
elif size == "l":
    final_amount += 25

if pepperoni == "y":
    if size == "s":
        final_amount += 2
    else:
        final_amount += 3

print(f"Your final bill is ${final_amount}")
