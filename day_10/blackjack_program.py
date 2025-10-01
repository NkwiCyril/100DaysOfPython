import random

bank = 1000


def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    return random.choice(cards)


def calculate_score(cards):
    return sum(cards)


player_cards = []
dealer_cards = []

start_game = input(
    "Do you want to play the game of  BlackJack? Type 'y' or 'n': ")

if start_game.lower() == 'y':

    print("Welcome to game of blackJack")
    print(f"Initial bank amount: ${bank}\n")

    while bank > 0:
        bet = int(input(f"How much do you bet? $"))
        max_total = 0

        print("")

        if bet > bank:
            print("Invalid bet")

            break

        bank -= bet
        player_cards = []

        print(f"AMOUNT IN BANK: ${bank}\n")

        # Deal initial cards for player
        for _ in range(2):
            player_cards.append(deal_card())
            dealer_cards.append(deal_card())

        print(
            f"Your cards: {player_cards}, Score={calculate_score(player_cards)}")
        print(f"Dealer revealed card: {dealer_cards[0]}\n")

        print("")

        while calculate_score(player_cards) < 21:
            choice = input("Would you like to 'HIT'[h] or 'Deal'[d]: ").lower()

            print("")

            if choice == 'h':
                player_cards.append(deal_card())

                if calculate_score(player_cards) == 21:
                    print("You win!")
                    print(
                        f"Your cards: {player_cards}, Score={calculate_score(player_cards)}")

                    bet *= 2  # double bank amount
                    bank += bet
                    break

                elif calculate_score(player_cards) > 21:
                    bank -= bet
                    print("You have lost. Dealer wins!")
                    print(
                        f"Your cards: {player_cards}, Score={calculate_score(player_cards)}")
                    print(
                        f"Dealers cards: {dealer_cards}, Score={calculate_score(dealer_cards)}")
                    break

                print(
                    f"Your cards: {player_cards}, Score={calculate_score(player_cards)}")

            elif choice == 'd':
                print(
                    f"Dealers cards: {dealer_cards}, Score={calculate_score(dealer_cards)}")

                if calculate_score(dealer_cards) == 21:
                    print("Dealer wins!")
                    bank -= bet

                if calculate_score(dealer_cards) < 16:
                    dealer_cards.append(deal_card())

                elif calculate_score(dealer_cards) >= 16:
                    max_total = max(calculate_score(player_cards),
                                    calculate_score(dealer_cards))

                    if max_total == calculate_score(player_cards):
                        print(f"You win! Score: {max_total}!")
                        bet *= 2  # double bank amount
                        bank += bet
                    else:
                        print(f"Dealer wins. Score: {max_total}")
                        bank -= bet

            else:
                print('Invalid choice')
else:
    print("exiting...")
