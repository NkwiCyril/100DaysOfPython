print("Welcome to the TIP Calculator")

bill = float(input("What is the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15? "))
num_people = int(input("How many people to split the bill? "))

def calculate_tip(bill, tip_percentage, num_people):
    tip = (bill * (tip_percentage/100)) / num_people
    return tip

print(f"Each person should pay: ${calculate_tip(bill, tip_percentage, num_people)}")