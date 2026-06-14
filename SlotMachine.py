# Python Slot Machine
import random 
def spin_row():
    symbols=["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("|".join(row)) 

def get_payout():
    pass

def main():
    balance=100
    print("*************************")
    print("Welcome to python slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance>0:
        print(f"Current balance: ${balance}")
        bet=input("Place your bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        bet=int(bet)
        if bet>balance:
            print("Insufficient money!")
            continue
        if bet<=0:
            print("Bet must be greater than 0")
            continue
        balance-=bet
        row=spin_row()
        print("Spinning..\n")
        print_row(row)
if __name__=='__main__':
    main()