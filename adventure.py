import time
import random
import string


def string_input(prompt, option1, option2):
    while True:
        option = input(prompt).lower()
        if option == option1 or option == option2:
            return option
        print_pause(f'Option {option} is invalid. Try again!')


def print_pause(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.2)
        time.sleep(.025)
    print("\n")


def intro():
    things = []
    print_pause("You find yourself standing in an abandoned"
                " village with fog.")
    print_pause("Rumor has it that two strange monsters"
                " are somewhere, around here.")
    print_pause("In front of you is silent house with the front door open.")
    print_pause("To your right is an alley from where "
                "you can hear a strange radio noise.")
    go_main(things)


def where_to_go(things):
    if 'pistol' in things:
        print_pause("You have a pistol and a knife in your inventory")
    else:
        print_pause("You have only a knife in your inventory.")
    choice1 = string_input("Enter '1' to enter the house. Enter '2' "
                           "to go to the alley\n", '1', '2')
    if choice1 == '1':
        go_house(things)
    elif choice1 == '2':
        go_alley(things)


def go_main(things):
    if 'already_in_house' in things and 'already_in_alley' in things:
        if 'medicine' not in things and 'injuries' in things:
            print_pause("You defeated both monsters but can't"
                        " beat the game with these injuries!")
            where_to_go(things)
        else:
            print_pause("You manage to kill both monsters!")
            print_pause("You beat the game, CONGRATULATIONS!")
            play_again()
    else:
        where_to_go(things)


def knife_in_house(things):
    if 'pistol' not in things:
        print_pause("You have only your knife to fight.")
    elif 'pistol' in things:
        print_pause("You chose fight with your knife!")
    rand1 = ["0", "1"]
    rand1 = random.choice(rand1)
    if rand1 == '0':
        print_pause("Unfortunately, your knife"
                    " was not effective for combat.")
        print_pause("The game is over.")
        play_again()
    elif rand1 == '1':
        print_pause("You fought bravely and managed to kill"
                    " the monster with your knife.")
        print_pause("Unfortunately, you were left with"
                    " some injuries after the battle.")
        things.append('injuries')
        things.append('already_in_house')
        go_upstairs(things)


def go_house(things):
    if 'already_in_house' in things:
        print_pause("The monster's body remains on the ground.")
        go_upstairs(things)
    else:
        if 'pistol' in things:
            print_pause("You enter the house.")
            print_pause("You encountered the other monster.")
            print_pause("The monster is coming to attack you.")
            choice2 = string_input("Enter '1' to use the knife "
                                   "or enter '2' to"
                                   " use the pistol to attack the "
                                   "monster.\n", '1', '2')
            if choice2 == '2':
                print_pause("You fought bravely and managed to kill"
                            " the monster with your pistol.")
                print_pause("Unfortunately, you were left with"
                            " some injuries after the battle.")
                things.append('injuries')
                things.append('already_in_house')
                go_upstairs(things)
            elif choice2 == '1':
                knife_in_house(things)
        elif 'pistol' not in things:
            print_pause("You enter the house.")
            print_pause("You encountered one of the monsters!")
            print_pause("The monster is coming to attack you.")
            knife_in_house(things)


def go_upstairs(things):
    print_pause("What do you wanna do?")
    choice3 = string_input("Enter '1' to leave the house."
                           " Enter '2' to go upstairs look for "
                           "something more.\n", '1', '2')
    if choice3 == '1':
        print_pause("You leave the house.")
        go_main(things)
    elif choice3 == '2':
        if 'medicine' not in things:
            print_pause("You go upstairs and found some medic kit.")
            print_pause("You can now leave the house with more "
                        "health and tranquility.")
            things.append('medicine')
            go_main(things)
        elif 'medicine' in things:
            print_pause("You go upstairs and realizes that there are"
                        " no more items left.")
            go_main(things)


def alley_choice(things):
    choice4 = string_input("Enter '1' to attack the "
                           "monster with your knife. "
                           "Enter '2' to attack the monster "
                           "with the pistol.\n", '1', '2')
    if choice4 == '1':
        print_pause("You manage to kill the monster with your knife.")
        print_pause("You check the pistol.")
        print_pause("You make sure the pistol is reloaded and working.")
        things.append('pistol')
        print_pause("You leave the alley.")
        things.append('already_in_alley')
        go_main(things)
    elif choice4 == '2':
        rand2 = ["0", "1", "2"]
        rand2 = random.choice(rand2)
        if rand2 == "0":
            print_pause("You realizes that the pistol has only"
                        " one bullet left.")
            print_pause("You manage to kill the monster with your pistol"
                        " with a 'headshot'.")
            print_pause("You make sure the pistol is reloaded"
                        " and working.")
            things.append('pistol')
            print_pause("You leave the alley.")
            things.append('already_in_alley')
            go_main(things)
        elif rand2 == "1" or rand2 == "2":
            print_pause("You realizes that the pistol has only"
                        " one bullet left.")
            print_pause("That one bullet was not enough"
                        " to kill the monster.")
            print_pause("The monster attacks you and you die.")
            print_pause("The game is over.")
            play_again()


def go_alley(things):
    if 'already_in_alley' in things:
        print_pause("The monster's body remains on the ground.")
        print_pause("There is nothing more to do here.")
        print_pause("You leave the alley.")
        go_main(things)
    else:
        if 'medicine' not in things and 'injuries' in things:
            print_pause("You enter in the alley following the radio noise.")
            print_pause("You can see a pistol near the radio.")
            print_pause("A monster wounded with two pistol shots "
                        "emerges from the shadows.")
            print_pause("Apparently your wounds are worse than his "
                        "and you can't reach the pistol.")
            print_pause("The monster attacks you and you die.")
            print_pause("The game is over.")
            play_again()
        else:
            print_pause("You enter in the alley following the radio noise.")
            print_pause("You can see a pistol near the radio, on the floor.")
            print_pause("A monster wounded with two pistol shots "
                        "emerges from the shadows.")
            print_pause("You manage to get the pistol before the monster "
                        "attacks you.")
            print_pause("What do you wanna do?")
            alley_choice(things)


def play_again():
    choice5 = string_input("Do you wanna to play again: Pres 'y' for"
                           " yes or 'n' for no.\n", 'y', 'n')
    if choice5 == 'y':
        intro()
    elif choice5 == 'n':
        print("Thanks for playing! Goodbye!")
        exit(0)


intro()
