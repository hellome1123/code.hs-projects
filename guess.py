import random

# library that we use in order to choose
# on random words from a list of words

name = input("What is your name? ")
# Here the user is asked to enter the name first

print("Good Luck ! ", name)

repeat = True
while repeat == True :
    fruits =  ['apple', 'olive', 'tomato', 'melon', 'litchi', 
    'mango', 'lime', 'kiwi', 'grapes', 'cherry',
    'banana', 'apricot', 'cucumber', 'guava', 'mulberry',
    'orange', 'papaya', 'pear', 'peach', 'berry']

    animals = ['ants', 'hippo', 'panda', 'giraffe', 'bat', 'bear',
    'catfish', 'cheetah', 'lizard', 'wolf', 'zebra', 'eagle',
    'cobra', 'goose', 'penguin', 'frog', 'mouse', 'flamingo',
    'rabbit', 'crow', 'whale', 'lion', 'monkey', 'ostrich',
    'peacock', 'raccoon', 'rhinoceros', 'sheep', 'dogs',
    'squirrel', 'tiger', 'vulture']

    accessories = ['ring', 'bangle', 'lipstick', 'handbag', 'crown',
    'necklace', 'watch', 'caps', 'glasses', 'wallet',
    'belts', 'comb', 'pendent', 'earring', 'scarf',
    'backpack', 'keychain', 'hairpin', 'shoes', 'hats',
    'jacket', 'boots', 'socks', 'stocking', 'muffler',
    'gloves', 'umbrella', 'ribbon']

    stationary = ['notebook', 'tape', 'pencil', 'eraser', 'sharpener',
    'files', 'fevicol', 'inkpot', 'chalk', 'duster',
    'glue', 'paper', 'cutter', 'chart', 'colours',
    'stapler', 'marker', 'staples', 'clips', 'calculator',
    'envelope', 'register']

    words = fruits + animals + accessories + stationary
    # Function will choose one random word from this list of words
    word = random.choice(words)
    print("Your word has", len(word), "letters.")
    # Game would randomly choose words

    print()

    if word in fruits:  # Give category of word
        print("Your word is a Fruit.")
    elif word in accessories:
        print("Your word is related to Accessory.")
    elif word in stationary:
        print("Your word is related to Stationary.")
    elif word in animals:
        print("Your word is an Animal")
    print("Guess the characters")

    guesses = ''

    # any number of turns can be used here
    turns = 5

    while turns > 0:

        # counts the number of times a user fails
        failed = 0

        # all characters from the input word taking one at a time.
        for char in word:

            # comparing that character with the character in guesses
            if char in guesses:
                print(char)

            else:
                print("_")

                # for every failure 1 will be incremented in failure
                failed += 1

        if failed == 0:
            # user will win the game if failure is 0 and 'You Win' will be given as output
            print("You Win")

            # this print the correct word
            print("The word is: ", word)
            break

        # if user has input the wrong alphabet then it will ask user to enter another alphabet
        guess = input("guess a character:")

        # every input character will be stored in guesses
        guesses += guess

        # check input with the character in word
        if guess not in word:

            turns -= 1

            # if the character doesn't match the word then "Wrong" will be given as output
            print("Wrong")

            # this will print the number of turns left for the user
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Loose")
                play_again = input("Would you like to play again? Type Y for yes and N for No!")
                if play_again == "N":
                    repeat = False
