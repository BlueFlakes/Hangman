import random
import time
import datetime

color = {
    'white':    "\033[1,37m",
    'yellow':   "\033[1,33m",
    'green':    "\033[1,32m",
    'blue':     "\033[1,34m",
    'cyan':     "\033[1,36m",
    'red':      "\033[1,31m",
    'magenta':  "\033[1,35m",
    'black':    "\033[1,30m",
    'darkwhite':  "\033[0,37m",
    'darkyellow': "\033[0,33m",
    'darkgreen':  "\033[0,32m",
    'darkblue':   "\033[0,34m",
    'darkcyan':   "\033[0,36m",
    'darkred':    "\033[0,31m",
    'darkmagenta': "\033[0,35m",
    'darkblack':  "\033[0,30m",
    'off':        "\033[0,0m"
}
yellow = "\033[1;33m"
darkblue = "\033[0;34m"
red = "\033[1;31m"
off = "\033[0;0m"
darkcyan = "\033[0;36m"
darkgreen = "\033[0;32m"
darkmagenta = "\033[0;35m"
darkwhite = "\033[0;37m"
darkyellow = "\033[0;33m"
blue = "\033[1;34m"
darkred = "\033[0;31m"

repair_sortowanie = []
highscores = []
today = datetime.date.today()
hangman = []
hangman_looks = [
"""
               +---+
               |   |
            	   |
            	   |
            	   |
                   |
            =========
          5 LIVES LEFT
""",
"""
               +---+
               |   |
               O   |
               |   |
            	   |
                   |
            =========
          4 LIVES LEFT
""",
"""
               +---+
               |   |
               O   |
              /|   |
            	   |
                   |
            =========
          3 LIVES LEFT
""",
"""
               +---+
               |   |
               O   |
              /|\  |
            	   |
                   |
            =========
          2 LIVES LEFT
""",
"""
               +---+
               |   |
               O   |
              /|\  |
              /    |
                   |
            =========
          1 LIFE LEFT
""",
"""
               +---+
               |   |
               O   |
              /|\  |
              / \  |
                   |
            =========
          YOU ARE DEAD
""",
"""
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ ___
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  |
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
""",

]

with open('countries_and_capitals.txt') as f:  # read the file
    lines = f.readlines()
lines = [line.rstrip('\n') for line in open('countries_and_capitals.txt')]  # remove '\n' from the end of a pair
pair = random.choice(lines).upper()  # choose random pair from the list
pair2 = pair.partition(" | ")[0:5]  # splits the pair into: [capital, separator, country]
hangman = []
used_letters = []
chosen_capital = pair2[2]
start_time = time.time()  # starting the clock

print(chosen_capital)
for i in range(len(chosen_capital)):
    hangman.append("_ ")


def sorting_the_highscore(length_of_game_time, output):
    highscores = output
    repair_sortowanie = length_of_game_time

    for i in range(len(repair_sortowanie)):
        for q in range(len(repair_sortowanie)):
            if repair_sortowanie[q] > repair_sortowanie[i]:
                save_HighS_for_replace = repair_sortowanie[i]
                repair_sortowanie[i] = repair_sortowanie[q]
                repair_sortowanie[q] = save_HighS_for_replace
                sort_second_list = highscores[i]
                highscores[i] = highscores[q]
                highscores[q] = sort_second_list
    highscores = highscores[:10]
    repair_sortowanie = repair_sortowanie[:10]


def guessing_a_word_correctly():
    print("YOU WIN, the capital was " + darkmagenta + "%s" % chosen_capital + off)
    print("It's the capital of " + darkyellow + "%s" % pair2[0] + off)
    game_time = ("%.2f" % (time.time() - start_time))
    print("It took you %s seconds" % game_time)  # showing the time
    print("It took you %s guesses" % guesses_number)

#               ----------------------------------------------------------------
    highscores.append("")
    highscores[len(highscores) - 1] = "%s seconds" % game_time + " | " + "Guesses: #%s" % guesses_number + " | " + name + " | " + str(today)
    repair_sortowanie.append(float(game_time))
    if len(highscores) > 1: # sort the elements of highscores list then sort second list in the way of first
        sorting_the_highscore(repair_sortowanie, highscores )
    print(red + "\n" + "HIGHSCORES:" + off)
    print("Position | Seconds | Guesses | Name | Date" + '\n')
    print('\n'.join(highscores), end = "\n")
    answer = ""
    while answer not in ["Y","N"]:
        answer = input('\n' + "Would you like to play again? (Y/N)").upper()
    if answer == "N":
        gameplay = 1
        return gameplay
    else:
        gameplay = 0
        return gameplay


def guessing_a_word_incorrectly():
    print (red + "Wrong word!" + off)
    print (hangman_looks[lives])
    if lives > 4:
        print(red + "GAME OVER" + off)
        print(darkgreen + "The correct word was" + off, red + "%s" % chosen_capital + off)
        answer = ""
        while answer not in ["Y", "N"]:
            answer = input('\n' + "Would you like to play again? (Y/N): ").upper()
        if answer == "N":
            gameplay = 1
            return gameplay


def guessing_a_letter_correctly():
    counter = 0
    element_pos = []
    for i in chosen_capital:  # Correct letter replaces the '_' in our word to guess
        if i == guess:
            element_pos.append(counter)
        counter = counter + 1
    if len(element_pos) > 0:  # it replaces the '_' with typed letter
        c = 0  # position counter
        for i in element_pos:
            a = element_pos[c]
            hangman.pop(a)
            hangman.insert(a, guess)
            c = c + 1  # counter value rises by 1
        # Removing the blank space:
    if " " in chosen_capital:  # if there is a blank in the city name
        counter1 = 0  # counter that checks every single letter in a city name
        element_pos1 = [] #list that cotains the position of blank space
        for i in chosen_capital:
            if i == " ":
                element_pos1.append(counter1)  # if a letter in a word is a blank space, it's position is added to the list
            counter1 = counter1 + 1
        if len(element_pos1) > 0:
            c1 = 0
            for i in element_pos1:
                a1 = element_pos1[c1]
                hangman.pop(a1)  # removes '_' where blank space should be
                hangman.insert(a1, " ")  # inserts blank space in that place
                c1 = c1 + 1


def guessing_a_letter_incorrectly():
    print(red + 'Wrong letter' + off)
    if lives > 1:
        print(hangman_looks[lives])
        print(darkcyan + "Tip: A capital of %s" % pair2[0] + off)
    else:
        print(hangman_looks[lives])
    if lives > 4:
        print(red + "GAME OVER" + off)
        print(darkgreen + "The correct word was" + off, red + "%s" % chosen_capital + off)
        answer = ""
        while answer not in ["Y","N"]:
            answer = input('\n' + "Would you like to play again? (Y/N)").upper()
        if answer == "N":
            gameplay = 1
            return gameplay


def main():
    lives = -1
    gameplay = 0
    records = 0
    while gameplay == 0:
        print(darkred + (hangman_looks[6]) + off)
        guesses_number = 0
        print(
            "Welcome to the great HANGMAN game.\
            \nAll you have to do is to guess a name of random world capital city.\
            \nGood luck!\n"
        )
        name = input(blue + "What is your name: " + off)
        while lives < 5:
            print(yellow + "Your capital is: " + off + darkblue + ' '.join(hangman) + off)
            hangman2 = (''.join(hangman))
            if hangman2 == chosen_capital: #winning while the whole word is made out of collected letters
                gameplay = guessing_a_word_correctly()
                break
            print (darkwhite + "Used letters: " + (" ".join(used_letters)) + off)
            guess = input(darkblue + "Guess a letter or a whole word: " + off).upper()  # Get a letter or a word
            if guess in used_letters:  # Checking if letter was used before
                print ("You've already used this letter!")
                guesses_number = guesses_number + 1
                pass
            if len(guess) == 1:  # guessing a letter
                if guess not in used_letters:
                    guesses_number = guesses_number + 1
                    used_letters.append(guess)  # Adding a letter to the list of used letters
                    if guess in chosen_capital:  # If the letter is correct
                        gameplay = guessing_a_letter_correctly()

                    elif guess not in chosen_capital:  # if the letter is incorrect
                        guesses_number = guesses_number + 1
                        lives = lives + 1
                        gameplay = guessing_a_letter_incorrectly()
            if len(guess) > 1:   # if you typed a word, instead of a letter
                guesses_number = guesses_number + 1
                if guess == chosen_capital:  #if typed the word is correct
                    #lives = lives + 1
                    gameplay = guessing_a_word_correctly()
                    break
                if guess != chosen_capital:  #if the word is incorrect
                    lives = lives + 1
                    gameplay = guessing_a_word_incorrectly()
main()
