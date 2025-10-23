import random
from game_data import influencers

final_score = 0


def choose_influencers():

    to_be_compared = []

    while True:

        first_choice = random.choice(influencers)
        second_choice = random.choice(influencers)

        first_choice_name = first_choice["name"]
        second_choice_name = second_choice["name"]

        if first_choice_name == second_choice_name:
            second_choice = random.choice(influencers)
        else:
            to_be_compared.append(first_choice)
            to_be_compared.append(second_choice)

            break

    return to_be_compared


while True:

    choosen_influencers = choose_influencers()

    letter_options = ["a", "b"]

    first_option = choosen_influencers[0]
    second_option = choosen_influencers[1]

    print(
        f"Who has the highest number of Instagram followers?\tFinal Score: {final_score}")

    choice = input(
        f"A = {first_option["name"]} VS B = {second_option["name"]}: ").lower()

    if choice not in letter_options:

        print("Invalid option! Choose 'A' or 'B'")

        break
    else:

        if (choice == "a" and first_option["followers"] > second_option["followers"]) or (choice == "b" and first_option["followers"] < second_option["followers"]):

            print("You are correct!")

            final_score += 1

        else:

            print("You are incorrect")

            break
