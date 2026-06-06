# Collection = single "variable" used to store multiple values

# fruits=("apple","banana","orange","grapes","kiwi","mango","leechee")

# List = [] ordered and changeable. Duplicate ok

# print(fruits[1])
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("orange" in fruits)
# print("pomegranate" in fruits)
# fruits.append("blackberry")
# fruits.remove("orange")
# fruits.insert(0,"cherry")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits)
# print(fruits.index("kiwi"))
# print(fruits.count("apple"))
# fruits[3]="pineapple"
# for fruit in fruits:
#     print(fruit)


# Set = {} unoredered and immutable, but Add/Remove ok. No duplicates
# print(len(fruits))
# print(dir(fruits))
# print(help(fruits))
# print(fruits[0])
# print("pineapple" in fruits)
# fruits.add("coconut")
# fruits.remove("orange")
# fruits.pop()
# fruits.clear()
# print(fruits)

# Tuple = () ordered and unchangeable. Duplicates ok, but faster

# print(fruits)
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits.index("apple"))
# print(fruits.count("apple"))
# for fruit in fruits:
#     print(fruit)

#Shopping cart program

# foods=[]
# prices=[]
# total=0

# while True:
#     food=input("Enter a food to buy (q to quit): ")
#     if food.lower()=="q":
#         break
#     else:
#         price=float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("--------YOUR CART--------")
# for food in foods:
#     print(food,end=" ")

# for price in prices:
#     total+=price
# print()
# print(f"Your total is: ${total}")

# Two-Dimensional (2D) Lists: -> A collection is made of number of collections

# groceries=[["apple","orange","mango","cherry"],
#            ["Tomato","Carrot","Potato"],
#            ["Chicken","Mutton","Fish"]]
# # print(groceries[0][3])
# for collection in groceries:
#     for food in collection:
#         print(food,end=" ")
#     print()

num_pad=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()