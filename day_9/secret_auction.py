import os

bids = {}
highest_bid = 0
winner = ""

print("Welcome to the secret auction program.")

while True: 
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if more_bidders.lower() == "no":
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

print("Bids:", bids)

for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder
        
print(f"The winner is {winner} with a bid of ${highest_bid}.")