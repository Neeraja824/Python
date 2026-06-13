# if __name__ == __main__: 
# This script can be imported or run standalone
# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular,
#                helps readability,
#                leaves no global variables,
#                avoid unintended exection)
# ex.library = import library for functionality when running library directly,display a help page

# print(dir())
# print(__name__)

# from Script2 import *
def favorite_food(food):
    print(f"My favourite food is {food}")

def main():
    print("This is script1")
    favorite_food("KFC")
    print("Bye!!")
if __name__ == '__main__':
    main()
# print(__name__)