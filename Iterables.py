# Iterables = An object/collection that can return its elements one at a time, 
#             allowing it to be iterated over in a loop

# numbers=(1,2,3,4,5)
# for number in reversed(numbers):
#     print(number)

# sets can't be reversed
# fruits={"apple","orange","banana","coconut"}
# for fruit in fruits:
#     print(fruit)

# name="Aditya"
# for letter in name:
#     print(letter,end=" ")

# my_dict={"A":1,"B":2,"C":3,"D":4}
# for key,value in my_dict.items():
#     print(f"{key} : {value}")

# membership Operators = Used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set or dictionary)
#                        1.in 2.not in

# word="Apple"
# letter=input("Guess a letter in the secret word: ")
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")

# students={"Alice","Bob","Charlie","Eric"}
# student=input("Enter the name of a student: ")
# if student in students:
#     print(f"{student} is present")
# else:
#     print(f"{student} is absent")

# grades={"Alice":"A","Bob":"B","Charlie":"C","Eric":"D"}
# student=input("Enter the name of a student: ")
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

# email="lankaneeraja824gmail.com"
# if "@" in email and "." in email:
#     print("Valid Email!")
# else:
#     print("Invalid Email!")

# List comprehension = A concise way to create lists in python
#                      compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]

# doubles=[]
# for x in range(1,11):
#     doubles.append(x*2)
# print(doubles)

# name=[expression for value in iterable]

# doubles=[x*2 for x in range(1,11)]
# triples=[y*3 for y in range(1,16)]
# squares=[z*z for z in range(1,21)]
# cubes=[a*a*a for a in range(1,11)]
# print(doubles)
# print(triples)
# print(squares)
# print(cubes)

# fruits=["apple","orange","banana","coconut"]
# fruits=[fruit.capitalize() for fruit in fruits]
# print(fruits)

# name=[expression for value in iterable if condition]

# numbers=[1,2,-3,4,-5,6,-7,8,9,-10]
# even_num=[number for number in numbers if number%2==0]
# odd_num=[number for number in numbers if number%2!=0]
# pos_num=[number for number in numbers if number>=0]
# neg_num=[number for number in numbers if number<0]
# print(even_num)
# print(odd_num)
# print(pos_num)
# print(neg_num)