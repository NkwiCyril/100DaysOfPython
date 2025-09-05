# TODO A
# 1. Store all registered card numbers and pin codes in dictionary, registered_bank_cards
# 2. User input the card number
# 3. Check if card number in verified card numbers

registered_card_numbers = {
    "0000 0000 0000 0000": 1111,
    "2342 6456 2353 2353": 4821,
    "4532 1289 7744 9823": 9054,
    "5123 8945 2234 1098": 1278,
    "6789 3321 4567 8842": 6642,
    "3498 6723 9087 1234": 3807,
    "2200 9944 6655 3321": 5913,
}

def check_card_number(card_number):
    return card_number in registered_card_numbers

def check_pin_code(card_number, pin_code):
    return registered_card_numbers[card_number] == pin_code

while True:

    card_number = input("Insert your card number: ")

    if check_card_number(card_number):
        
        pin_code = int(input("Input your 4-digit PIN code: "))

        if check_pin_code(card_number, pin_code):
            print("Pin code is valid")
        else:
            print("Invalid pin code")
            break

    else:
        print("Card is not valid")
        break
