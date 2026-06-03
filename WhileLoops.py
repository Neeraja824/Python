#While Loop = Execute some code WHILE some condition remains true

name=input("Enter your name: ")
while name == "":
    print("You did not enter your name..")
    name=input("Enter your name: ")
print(f"Welcome {name}")

age=int(input("Enter your age: "))
while age<0:
    print("Age can't be negative..")
    age=int(input("Enter your age: "))
print(f"You are {age} years old!..")

food=input("Enter a food you most like (q for quit): ")
while food == "q":
    print("You quit..")
    food=input("Enter a food you most like (q for quit): ")
print(f"I most liked food is: {food}")

num=int(input("Enter a number b/w 1 to 100: "))
while num <1 or num>100:
    print(f"{num} is not valid")
    num=int(input("Enter a number b/w 1 to 100: "))
print(f"You enter a number: {num}")