import random

print("Welcome to ROCK, PAPER, SCISSORS!")

num_rounds = int(input("How many rounds will you like to go? "))

rounds = 1

computer_points = 0
user_points = 0

while rounds <= num_rounds:

    print("\n==================================") 
    print(f"ROUND {rounds}") 
    print("==================================")

    rounds += 1

    computer_choice = random.choice(['r', 'p', 's'])
    user_choice = input("Rock 'r' Paper 'p' Scissors 's'? ")

    if computer_choice == 'r' and user_choice == 's':
        computer_points += 1

        print(f"Computer: {computer_choice.upper()} VS User: {user_choice.upper()}")
        print("Computer wins\n")
    elif computer_choice == 's' and user_choice == 'r':
        user_points += 1

        print(f"Computer: {computer_choice.upper()} VS User: {user_choice.upper()}")
        print("User wins\n")
    elif computer_choice == 'p' and user_choice == 'r':
        computer_points += 1

        print(f"Computer: {computer_choice.upper()} VS User: {user_choice.upper()}")
        print("Computer wins\n")
    elif computer_choice == 'r' and user_choice == 'p':
        user_points += 1

        print(f"Computer: {computer_choice.upper()} VS User: {user_choice.upper()}")
        print("User wins\n")
    elif computer_choice == 's' and user_choice == 'p':
        print(f"Computer: {computer_choice.upper()} VS User: {user_choice.upper()}")
        print("Computer wins\n")
    elif computer_choice == 'p' and user_choice == 's':
        user_points += 1

        print(f"Computer: {computer_choice.upper()} VS User: {user_choice.upper()}")
        print("User wins\n")
    elif computer_choice == user_choice:
        print(f"Computer: {computer_choice.upper()} VS User: {user_choice.upper()}")
        print("It is a tie!\n")
    else:
        print("Invalid input\n")


print(f"\n{rounds - 1} rounds completed.")

print(f"COMPUTER: {computer_points}")
print(f"USER: {user_points}")

if computer_points > user_points:
    print(f"COMPUTER WINS with {computer_points - user_points} more!")
elif user_points > computer_points:
    print(f"USER WINS with {user_points - computer_points} more!")
else:
    print("It's a tie.")
