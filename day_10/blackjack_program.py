import random

# Initial bank
bank = 1000
total_bets = 0
total_won = 0


def deal_card():
    """Return a random card from a standard deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
             10, 10, 11]  # 10 = J, Q, K; 11 = Ace
    return random.choice(cards)


def calculate_score(cards):
    """Return score, adjusting for Aces (11 or 1)."""
    score = sum(cards)
    # Adjust Ace value if over 21
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score


def print_summary():
    """Print final summary when game ends."""
    print("\n===== GAME OVER =====")
    print(f"Total bets placed: ${total_bets}")
    print(f"Total won: ${total_won}")
    print(f"Final bank amount: ${bank}")
    print("=====================\n")


# Start Game
start_game = input("Do you want to play Blackjack? Type 'y' or 'n': ")

if start_game.lower() == 'y':
    print("\nWelcome to Blackjack!")
    print(f"Initial bank amount: ${bank}\n")

    while bank > 0:
        bet = input(f"How much do you bet? (or type 'q' to quit): ")

        if bet.lower() == 'q':  # player chooses to leave with winnings
            print("You chose to exit the game.")
            break

        # Validate bet
        if not bet.isdigit() or int(bet) <= 0:
            print("Invalid bet amount! Try again.\n")
            continue

        bet = int(bet)

        if bet > bank:
            print("Not enough money in the bank!\n")
            continue

        bank -= bet
        total_bets += bet

        player_cards = [deal_card(), deal_card()]
        dealer_cards = [deal_card(), deal_card()]

        game_over = False

        print(
            f"\nYour cards: {player_cards}, score = {calculate_score(player_cards)}")
        print(f"Dealer shows: {dealer_cards[0]}\n")

        # Player's turn
        while not game_over:
            if calculate_score(player_cards) == 21:
                print("Blackjack! You win!")
                
                winnings = bet * 2
                bank += winnings
                total_won += winnings
                
                game_over = True
                
                break

            choice = input(
                "Would you like to 'Hit' [h] or 'Stand' [s]: ").lower()

            if choice == 'h':
                player_cards.append(deal_card())
                print(
                    f"Your cards: {player_cards}, score = {calculate_score(player_cards)}")

                if calculate_score(player_cards) > 21:
                    print("You busted! Dealer wins.")
                    game_over = True
            
            elif choice == 's':
                break
            
            else:
                print("Invalid choice. Please type 'h' or 's'.")

        # Dealer's turn
        if calculate_score(player_cards) <= 21 and not game_over:
            print(
                f"\nDealer's cards: {dealer_cards}, score = {calculate_score(dealer_cards)}")
            while calculate_score(dealer_cards) < 17:
                dealer_cards.append(deal_card())
                print(
                    f"Dealer draws a card: {dealer_cards}, score = {calculate_score(dealer_cards)}")

            dealer_score = calculate_score(dealer_cards)
            player_score = calculate_score(player_cards)

            if dealer_score > 21 or player_score > dealer_score:
                print("You win this round!")
                
                winnings = bet * 2
                bank += winnings
                total_won += winnings
            
            elif dealer_score == player_score:
                print("It's a draw! Your bet is returned.")
                bank += bet
            
            else:
                print("Dealer wins this round.")

        print(f"\nYour bank: ${bank}\n")

        # If player has no money left
        if bank <= 0:
            print("You lost all your money!")
            break

    # Final summary
    print_summary()

else:
    print("Exiting game...")
