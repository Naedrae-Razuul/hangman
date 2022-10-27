import random;import time;import os

# storing strings randomly chosen..
bank = ['tiger', 'cat', 'dog', 'spider', 'insect', 'hello']
# right here
global x
x = random.choice(bank)
# counts characters in string chosen
y = len(x)


special_chars = ['', ' ', ',', '<', '.', '>', '/', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
remainder = "-"*y
# stores hangman graphics

graphic8 =    ("  -----\n"
         "  |   |\n"
         "      |\n"
         "      |\n"
         "      |\n"
         "    -----")
graphic7 =     ("  -----\n"
          "  |   |\n"
          "  o   |\n"
          "      |\n"
          "      |\n"
          "    -----")
graphic6 =    ("  -----\n"
         "  |   |\n"
         "  o   |\n"
         "  |   |\n"
         "      |\n"
         "    -----")
graphic5 =     ("  -----\n"
          "  |   |\n"
          "  o / |\n"
          "  |   |\n"
          "      |\n"
          "    -----")
graphic4 =    ("  -----\n"
         "  |   |\n"
         "\ o / |\n"
         "  |   |\n"
         "      |\n"
         "    -----")
graphic3 =    ("  -----\n"
         "  |   |\n"
         "\ o / |\n"
         "  |   |\n"
         "      |\n"
         "    -----")
graphic2 =      ("  -----\n"
           "  |   |\n"
           "\ o / |\n"
           "  |   |\n"
           "   \  |\n"
           "    -----")
graphic1 =     ("  -----\n"
          "  |   |\n"
          "\ o / |\n"
          "  |   |\n"
          " / \  |\n"
          "    -----")


# checks points everytime, and displays the man.. hanging..(?)
def hangman():
    if points == 8:
        print(graphic8)
    if points == 7:
        print(graphic7)
    if points == 6:
        print(graphic6)
    if points == 5:
        print(graphic5)
    if points == 4:
        print(graphic4)
    if points == 3:
        print(graphic3)
    if points == 2:
        print(graphic2)
    if points == 1:
        print(graphic1)
        print("\n\nYou lost!"); time.sleep(2)
        exit


points = 8
while remainder != x:
    hangman()
    print("\n" + remainder)
    guess = input("\n\nGuess a letter: ")


    cnt = len(guess)

    # check if input is greater than 1 character
    if cnt > 1:
        print("\nMust use only one letter\n"); time.sleep(1)
        os.system('cls')
        continue
    # check if input has special characters
    if guess in special_chars:
        print("\nMust only use letters\n"); time.sleep(1)
        os.system('cls')
        continue

    # if correct..
    if guess in x:
        print('\ncorrect!\n'); time.sleep(1)
        os.system('cls')
        pos = x.rfind(guess)
        remainder = remainder[:pos]+guess+remainder[pos+1:]

    # if guess is.. guessed? incorrectly
    else:
        print("\nGuess again! (incorrect)\n"); time.sleep(1)
        points = points - 1
        os.system('cls')

    if points == 1:
        print(graphic1)
        print("\n\nYou lost!");
        time.sleep(2)
        exit

# you won! Yay!
print("The word was: " + x)
print("\ncongrats! You won!!"); time.sleep(2)