# Hangman in python

import random
words=["apple","orange","banana","coconut","pineapple","Apple", 
       "Banana", "Orange", "Mango", "Grapes","Pineapple", "Papaya", 
       "Guava", "Watermelon", "Muskmelon","Strawberry", "Blueberry", 
       "Raspberry", "Blackberry", "Cherry","Peach", "Pear", "Plum", 
       "Apricot", "Kiwi","Pomegranate", "Lemon", "Lime", "Coconut", 
       "Avocado","Fig", "Date", "Lychee", "Dragon Fruit", "Passion Fruit",
       "Jackfruit", "Star Fruit", "Custard Apple", "Sapodilla", "Mulberry",
       "Cranberry", "Gooseberry", "Tamarind", "Persimmon", "Pomelo",
       "Mandarin", "Clementine", "Tangerine", "Durian", "Rambutan",
       "Longan", "Mangosteen", "Breadfruit", "Jujube", "Soursop"]

# dictionary of key: ()
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}
    
def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words)
    hint=["_"] * len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running=True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess=input("Enter a letter: ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            wrong_guesses+=1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running=False
        elif wrong_guesses>=len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running=False
if __name__ =='__main__':
    main()