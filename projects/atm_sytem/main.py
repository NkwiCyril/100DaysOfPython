registered_card_numbers = {
    "0000": {
        "name": "Nkwi Cyril Akinimbom",
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


def check_balance(card_number, choosen_amount):
    return registered_card_numbers[card_number]["balance"] > choosen_amount


ATM_HEADER = """
****************************************************
*                                                  *
*        █████╗ ████████╗███╗   ███╗               *
*       ██╔══██╗╚══██╔══╝████╗ ████║               *
*       ███████║   ██║   ██╔████╔██║               *
*       ██╔══██║   ██║   ██║╚██╔╝██║               *
*       ██║  ██║   ██║   ██║ ╚═╝ ██║               *
*       ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝               *
*                                                  *
*          SIMULATED PYTHON ATM MACHINE            *
****************************************************
"""

ATM_FOOTER = """
****************************************************
*            THANK YOU FOR USING PY-ATM!           *
****************************************************
"""

while True:
    print(ATM_HEADER)

    attempts = 2

    card_number = input("💳 Insert your card number: ").strip()
    card_in_session.append(card_number)

    if check_card_number(card_in_session[0]):
        print("\n" + "*" * 55)
        print(f"   ✅ WELCOME, {registered_card_numbers[card_number]['name']}!")
        print("*" * 55 + "\n")

        pin_verified = False

        while attempts > 0:
            attempts -= 1
            pin_code = int(input("🔑 Enter your 4-digit PIN code: "))

            if check_pin_code(card_number, pin_code):
                pin_verified = True
                break
            else:
                print("❌ Incorrect pin code\n")

        if attempts <= 0 and not pin_verified:
            print("⚠️  Too many incorrect attempts! Card removed.\n")
            card_in_session.pop()
            continue

        if pin_verified:
            amounts = [10000, 20000, 50000, 100000, 150000, "Key Amount"]
            options = []

            print("\n💵 Choose a withdrawal amount:\n")
            print("----------------------------------------------------")
            for i, amount in enumerate(amounts, start=0):
                print(f"  {i}. {amount}")
                options.append(i)
            print("----------------------------------------------------\n")

            while True:
                choice = int(input("👉 Your choice: "))

                if choice in options:
                    if choice == amounts.index("Key Amount"):
                        key_amount = int(input("Enter custom amount (XAF): "))

                        if check_balance(card_in_session[0], key_amount):
                            registered_card_numbers[card_in_session[0]]["balance"] -= key_amount
                            print("\n✅ Withdrawal successful!")
                            print(f"💰 Remaining Balance: {registered_card_numbers[card_in_session[0]]['balance']} XAF\n")

                            card_in_session.pop()
                            break
                        else:
                            print("⚠️ Insufficient balance!\n")

                    else:
                        if check_balance(card_in_session[0], amounts[choice]):
                            registered_card_numbers[card_in_session[0]]["balance"] -= amounts[choice]
                            print("\n✅ Withdrawal successful!")
                            print(f"💰 Remaining Balance: {registered_card_numbers[card_in_session[0]]['balance']} XAF\n")

                            card_in_session.pop()
                            break
                        else:
                            print("⚠️ Insufficient balance!\n")
                else:
                    print("❌ Invalid choice. Try again.")
                    continue

        print(ATM_FOOTER)

    else:
        print("❌ Invalid card number. Card removed.\n")
        card_in_session.pop()
