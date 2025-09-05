# TODO A
# 1. Store all registered card numbers and pin codes in dictionary, registered_bank_cards
# 2. User input the card number
# 3. Check if card number in verified card numbers

registered_card_numbers = {
    "0000": {
        "name": "John Doe",
        "pin_code": 0000,
        "balance": 10000000
    },
    "0000 0000 0000 0000": {
        "name": "Jane Smith",
        "pin_code": 1111,
        "balance": 10000000
    },
    "2342 6456 2353 2353": {
        "name": "Alice Johnson",
        "pin_code": 4821,
        "balance": 25000
    },
    "4532 1289 7744 9823": {
        "name": "Michael Brown",
        "pin_code": 9054,
        "balance": 73200
    },
    "5123 8945 2234 1098": {
        "name": "Sophia Davis",
        "pin_code": 1278,
        "balance": 15800
    },
    "6789 3321 4567 8842": {
        "name": "James Wilson",
        "pin_code": 6642,
        "balance": 99500
    },
    "3498 6723 9087 1234": {
        "name": "Olivia Martinez",
        "pin_code": 3807,
        "balance": 42100
    },
    "2200 9944 6655 3321": {
        "name": "Daniel Anderson",
        "pin_code": 5913,
        "balance": 86000
    },
}

card_in_session = []


def check_card_number(card_number):
    return card_number in registered_card_numbers


def check_pin_code(card_number, pin_code):
    return registered_card_numbers[card_number]["pin_code"] == pin_code


while True:

    attempts = 2

    print(f"Card in session (BEFORE): {card_in_session}")

    card_number = input("Insert your card number: ")

    card_in_session.append(card_number)

    print(f"Card in session (AFTER): {card_in_session}")

    if check_card_number(card_in_session[0]):

        print("\n***********************************************************")
        print(f"\t\tWELCOME {registered_card_numbers[card_number]["name"]}!")
        print("***********************************************************\n")

        pin_verified = False

        while attempts > 0:

            attempts -= 1

            pin_code = int(input("Input your 4-digit PIN code: "))

            if check_pin_code(card_number, pin_code):
                pin_verified = True
                break

            else:
                print("Incorrect pin code\n")

        if attempts <= 0 and not pin_verified:
            print("You have surpassed the number of attempts")
            print("Removing card...\n")

            card_in_session.pop()
            continue

        if pin_verified:
            print("Proceed with withdrawal...")

    else:
        print("Card is invalid")
        print("Removing card...\n")

        card_in_session.pop()
