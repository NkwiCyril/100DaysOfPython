# registered_card_numbers = {
#     "0000": {
#         "pin_code": 0000,
#         "balance": 10000000
#     },
#     "0000 0000 0000 0000": {
#         "pin_code": 1111,
#         "balance": 10000000
#     },
#     "2342 6456 2353 2353": {
#         "pin_code": 4821,
#         "balance": 25000
#     },
#     "4532 1289 7744 9823": {
#         "pin_code": 9054,
#         "balance": 73200
#     },
#     "5123 8945 2234 1098": {
#         "pin_code": 1278,
#         "balance": 15800
#     },
#     "6789 3321 4567 8842": {
#         "pin_code": 6642,
#         "balance": 99500
#     },
#     "3498 6723 9087 1234": {
#         "pin_code": 3807,
#         "balance": 42100
#     },
#     "2200 9944 6655 3321": {
#         "pin_code": 5913,
#         "balance": 86000
#     },
# }

# def check_pin_code(card_number, pin_code):
#     return registered_card_numbers[card_number]["pin_code"] == pin_code

# print(check_pin_code("0000 0000 0000 0000", 1111))


amounts = [10000, 20000, 50000, 100000, 150000, "Key Amount"]

print(amounts.index("Key Amount"))