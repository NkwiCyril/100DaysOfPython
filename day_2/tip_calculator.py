print("Welcome to the TIP Calculator")

bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
num_people = int(input("How many people to split the bill? "))

def calculate_tip(bill, tip, num_people):
    tip_percentage = tip / 100
    total_tip_amount = bill * tip_percentage
    total_bill = bill + total_tip_amount

    shared_bill = total_bill / num_people

    return shared_bill

print(f"Each person should pay: ${calculate_tip(bill, tip, num_people)}")