# Variables = A container for a value(string,integer,float,boolean). A variable behaves as if it was the value it contains
#Strings
first_name="Neeru"
print(f"Hello {first_name}")

#Integers
age=21
print(f"You are {age} years old")

#Float
price=24.05
print(f"The price is ${price}")

#Boolean
is_student=False
if is_student:
    print("You are a student")
else:
    print("You are not a student")
# print(f"Are you a student?: {is_student}")

#Typecasting = The process of converting a variable from one data type to another (str(),int(),float(),bool())
name="anu"
age=24
score=100.89
is_girl=True
# print(type(is_girl))
score=int(score)
print(score)
age=str(age)
age+="05"
print(age)
user="aditya"
user=bool(user)
print(user)

# input() = A function that prompts the user to enter data and returns the entered data as a string
name=input("what is your name?: ")
age=input("How old are you?: ")
age=int(age)
age+=1
print(f"Hello {name}!")
print(f"You are {age} years old")

#Area of rectangle program
length=float(input("Enter the length: "))
width=float(input("Enter the width: "))
area=length * width
print(f"The area is: {area}cm")

#Shopping cart program
item=input("What item would you like to buy?: ")
price=float(input("What is the price?: "))
quantity=int(input("How many would you like?: "))
total=price*quantity
print(f"You have bought {quantity} x {item}/s")
print(f"The Total cost is: {total}")









