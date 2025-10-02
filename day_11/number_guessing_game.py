import random

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

rand_number = random.randint(1, 100)

attempts = 0
guessed_correctly = False

def print_summary(outcome):
    if outcome:
        print("\n===== YOU WIN! =====")
        print(f"Total attempts: {attempts}/10")
        print("=====================\n")
    else:
        print("\n===== YOU LOSE! =====")
        print(F"The correct number is {rand_number}")
        print(f"Total attempts: {attempts}/10")
        print("=====================\n")        

while attempts < 10:

    choice = int(input("Guess the number: "))

    if choice == rand_number:
        print("You guessed correctly")

        guessed_correctly = True

        break

    elif choice > rand_number:
        print("Too High!")

        attempts += 1
    
    elif choice < rand_number:
        print("Too low!")

        attempts += 1


print_summary(guessed_correctly)