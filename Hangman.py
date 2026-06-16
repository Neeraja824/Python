# Hangman in python

import random

words = [
    "apple","orange","banana","coconut","pineapple",
    "mango","grapes","papaya","guava","watermelon",
    "muskmelon","strawberry","blueberry","raspberry",
    "blackberry","cherry","peach","pear","plum",
    "apricot","kiwi","pomegranate","lemon","lime",
    "avocado","fig","date","lychee","dragon fruit","passion fruit",
    "jackfruit","star fruit","custard apple","sapodilla","mulberry",
    "cranberry","gooseberry","tamarind","persimmon","pomelo",
    "mandarin","clementine","tangerine","durian","rambutan",
    "longan","mangosteen","breadfruit","jujube","soursop"
]

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
    answer = random.choice(words).lower()
    hint = ["_" if ch != " " else " " for ch in answer]
    wrong_guesses = 0
    guessed_letters = set()

    while True:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, ch in enumerate(answer):
                if ch == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            break

        if wrong_guesses == 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            break

if __name__ == "__main__":
    main()