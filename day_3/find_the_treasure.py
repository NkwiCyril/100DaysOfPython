print("Welcome to Treasure Island!")
print("Your mission is to find the treasure\n")

cross_road = input("You are at a cross road. Where do you want to cross? Left or Right?\n\tType 'left' or 'right'\n").lower()

if cross_road == 'right':

    print("You fell into a river. Game over!")

elif cross_road == 'left':

    wait_or_swim = input("You've come to a lake. There is an island in the middle of the lake.\n\tType 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()

    if wait_or_swim == "swim":

        print("You get attacked by an angry trout. Game Over!")
    
    elif wait_or_swim == "wait":
    
        house_color = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?\n").lower()

        if house_color == "red":
            print("It's a room full of fire. Game Over!")
        elif house_color == "blue":
            print("You enter a room of beasts. Game Over!")
        elif house_color == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Invalid input")
    else: 
        print("Invalid input")
else:
    print("Invalid input")
