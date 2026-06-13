from Script1 import *
# print(__name__)

def favorite_drink(drink):
    print(f"My favorite drink is {drink}")
def main():
    print("This is script2")
    favorite_food("Burger")
    favorite_drink("DryFruits juice")
    print("Goodbye!!")
if __name__ == '__main__':
    main()