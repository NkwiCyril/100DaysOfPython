import random

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
""")

words = [
    "apple", "book", "car", "fish", "home", "milk", "rain", "shoe", "tree", "water",
    "garden", "school", "friend", "planet", "silver", "market", "castle", "window", "bridge", "jungle",
    "awkward", "banquet", "crypt", "drought", "giraffe", "hyphen", "jigsaw", "oxygen", "rhythm", "zephyr"
]

number_of_lives = 6

random_word = "bean" # random.choice(words)

def check_letter_in_word(letter, word):
    if letter in word:
        return True
    else:
        return False

def generate_hangman(num_lives):
        if num_lives == 5:
                print('''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========
            ''')
        elif num_lives == 4:
            print('''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========
            ''')
        elif num_lives == 3:
            print('''
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                =========
            ''')
        elif num_lives == 2:
            print('''
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                =========
            ''')
        elif num_lives == 1:
            print('''
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
                =========
            ''')
        elif num_lives == 0:
            print('''
                _______
                |/      |
                |      (_)
                |      \|/
                |       |
                |      / \
                |
              __|___
            ''')

dashes_array = ["_" for _ in random_word]

while number_of_lives > 0:
    
    choosen_letters = ' '.join(dashes_array)
    
    print(f"Word to guess: {choosen_letters}")
    
    guessed_letter = input("Guess a letter: ")

    if check_letter_in_word(guessed_letter, random_word):
        print('''
            +---+
            |   |
                |
                |
                |
                |
            =========            
        ''')
        print(f"****************************{number_of_lives}/6 LIVES LEFT****************************")

        for i in range(0, len(random_word)):
            if random_word[i] == guessed_letter:
                dashes_array[i] = guessed_letter
        
        if "_" not in choosen_letters:
            print(f"***********************YOU GUESSED CORRECTLY! YOU WIN!**********************")
            break

    else:
        number_of_lives -= 1

        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")

        generate_hangman(number_of_lives)
        
        print(f"****************************{number_of_lives}/6 LIVES LEFT****************************")


        if number_of_lives <= 0 and "_" in dashes_array:
            print(f"***********************IT WAS {random_word}! YOU LOSE**********************")
            break