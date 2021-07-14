from random import randint

i = 0
a = 0
tries = 0
left_tries = 6
hits = 0
fail_condition = 6
huge_list = []
noun_list = []
hidden_word = ""
no_hits_message = "No hits. Try again. You have {} tries left."
play_again = "y"
is_a_game_running = True
f = open("nouns.txt", encoding="utf-8")


def convert(string):
    list1 = []
    list1[:0] = string
    return list1

"""
if is_a_game_running:
    for line in f:
        huge_list.extend(line.split())
    
    for x in huge_list:
        if x.isalpha() and len(x) > 2:
            noun_list.append(x)
    
    chosen_word = randint(0, 1524)
    number_letters = len(noun_list[chosen_word])
    the_word = (noun_list[chosen_word])
    the_word = convert(the_word)
    print(number_letters)
    print(the_word)
    
    while i < number_letters:
        hidden_word = hidden_word + "."
        i += 1
    
    hidden_word = convert(hidden_word)
    #print(hidden_word)
"""
while tries < fail_condition:
    if is_a_game_running:
        for line in f:
            huge_list.extend(line.split())

        for x in huge_list:
            if x.isalpha() and len(x) > 2:
                noun_list.append(x)

        chosen_word = randint(0, 1524)
        number_letters = len(noun_list[chosen_word])
        the_word = (noun_list[chosen_word])
        the_word = convert(the_word)
#        print(number_letters)
 #       print(the_word)

        while i < number_letters:
            hidden_word = hidden_word + "."
            i += 1

        hidden_word = convert(hidden_word)
        is_a_game_running = False
        # print(hidden_word)
    if tries == 0:
        print("""
  +---+
  |   |
      |
      |
      |
      |
=========""")
    if tries == 1:
            print("""
  +---+
  |   |
  O   |
      |
      |
      |
=========""")
    if tries == 2:
            print("""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""")
    if tries == 3:
            print("""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""")
    if tries == 4:
            print("""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""")
    if tries == 5:
            print("""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""")
    if tries == 6:
            print("""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""")
    print(hidden_word)
    guess = input("Make a guess:")
    a = 0
    hits = 0
    if len(guess) > 1 or not guess.isalpha() or not guess.islower():
        print("Please enter a valid lowercase letter")
        continue
    while a < number_letters:
       # if len(guess) > 1 or not guess.isalpha():
       #     print("Please enter a valid letter")
       #     guess = input("Make a guess:")
       #     continue
        word_letter = the_word[a]
        if word_letter == guess:
            hidden_word[a] = guess
            if hidden_word == the_word:
                if tries == 0:
                    print("""
  +---+
  |   |
      |
      |
      |
      |
=========""")
                if tries == 1:
                    print("""
  +---+
  |   |
  O   |
      |
      |
      |
=========""")
                if tries == 2:
                    print("""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""")
                if tries == 3:
                    print("""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""")
                if tries == 4:
                    print("""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""")
                if tries == 5:
                    print("""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""")
                if tries == 6:
                    print("""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""")

                print(hidden_word)
                print("YOU WIN")
                exit()
            a += 1
            hits += 1
        else:
            a += 1
        if hits == 0 and not a < number_letters:
            tries += 1
            left_tries -= 1
            a = 0
            if tries == 1:
                print("""
  +---+
  |   |
  O   |
      |
      |
      |
=========""")
            if tries == 2:
                print("""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""")
            if tries == 3:
                print("""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""")
            if tries == 4:
                print("""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""")
            if tries == 5:
                print("""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""")
            if tries == 6:
                print("""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""")
            if tries < 6:
                print(no_hits_message.format(left_tries))
                print(hidden_word)
            if tries == fail_condition:
                print(the_word)
                print("YOU LOSE")
                exit()
                """"
                play_again = input("Do tou want to play again? [y/n]")
                if play_again == "y":
                    is_a_game_running = True
                if play_again == "n":
                    exit()
                    """
            guess = input("Make a guess:")
            if len(guess) > 1 or not guess.isalpha() or not guess.islower():
                print("Please enter a valid lowercase letter")
                continue

