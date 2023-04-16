# Made by Nathaniel Masson /// 10/26/22, updated 4/16/23
#
#
import os
import random
import time
def start():
    # stores random word chosen from 'bank.txt' to a variable.
    randint = random.randint(0, 213)
    try:
        f = open("./bank.txt", 'r')
    except:
        print("You have yet to create a bank.txt file! Do so (in the same directory as this .py file), and the code"
              "will work!")
        extremely_hard_choice = input("\n\nPress enter to exit the program. Or, input 'yes' to restart!")
        if extremely_hard_choice == 'yes' or 'Yes':
            print("Restarting!!")
            time.sleep()
            start()
        else:
            print('Exiting!! (you suck)')
            time.sleep(2)
            exit()
    word = f.readlines()
    f.close()
    word = word[randint]
    
    # counts characters in the string chosen
    y = len(word)
    
    # exceptions
    special_chars = ['', ' ', ',', '<', '.', '>', '/', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    remainder = "-" * y
    
    # stores hangman graphics
    graphic = [("  -----\n"
                "  |   |\n"
                "      |\n"
                "      |\n"
                "      |\n"
                "    -----"),
               ("  -----\n"
                "  |   |\n"
                "  o   |\n"
                "      |\n"
                "      |\n"
                "    -----"),
               ("  -----\n"
                "  |   |\n"
                "  o   |\n"
                "  |   |\n"
                "      |\n"
                "    -----"),
               ("  -----\n"
                "  |   |\n"
                "  o / |\n"
                "  |   |\n"
                "      |\n"
                "    -----"),
               ("  -----\n"
                "  |   |\n"
                "\ o / |\n"
                "  |   |\n"
                "      |\n"
                "    -----"),
               ("  -----\n"
                "  |   |\n"
                "\ o / |\n"
                "  |   |\n"
                "      |\n"
                "    -----"),
               ("  -----\n"
                "  |   |\n"
                "\ o / |\n"
                "  |   |\n"
                "   \  |\n"
                "    -----"),
               ("  -----\n"
                "  |   |\n"
                "\ o / |\n"
                "  |   |\n"
                " / \  |\n"
                "    -----")]
    
    points = 0
    while remainder != word:
        print(graphic[points])
    
        print("\n" + remainder)
        guess = input("\n\nGuess a letter: ")
    
        cnt = len(guess)
    
        # check if input is greater than 1 character
        if cnt > 1:
            print("\nMust use only one letter\n");
            time.sleep(1)
            os.system('cls')
            continue
        # check if input has special characters
        if guess in special_chars:
            print("\nMust only use letters\n");
            time.sleep(1)
            os.system('cls')
            continue
    
        # if correct..
        if guess in word:
            print('\ncorrect!\n');
            time.sleep(1)
            os.system('cls')
            pos = word.rfind(guess)
            remainder = remainder[:pos] + guess + remainder[pos + 1:]
    
        # if guess is.. guessed? incorrectly
        else:
            print("\nGuess again! (incorrect)\n");
            time.sleep(1)
            points = points + 1
            os.system('cls')
    
        if points == 8:
            print("\n\nYou lost!");
            time.sleep(2)
            exit
    
    # you won! Yay!
    print("The word was: " + word)
    print("\ncongrats! You won!!");
    time.sleep(2)
start()
