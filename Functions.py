# Function = A block of reusable code place() after the function name to invoke it

# def fun(name,age):
#     print(f"Hello {name}! You are {age} years old.")
# fun("Purna",35)
# fun("Uma",18)
# fun("Aditya",21)

# def display_invoice(username,amount,due_date):
#     print(f"Hello {username}!")
#     print(f"Your bill of ${amount:.3f} is due: {due_date}")
# display_invoice("Purna",50000,"01/01")
# display_invoice("Uma",30000,"03/04")
# display_invoice("Aditya",10000,"05/24")
# display_invoice("Neeru",20000,"10/05")

# return = It is a statement to end a function and send a result back to the caller

# def add(a,b):
#     c=a+b 
#     return c 

# def subtract(a,b):
#     c=a-b 
#     return c 

# def multiply(a,b):
#     c=a*b 
#     return c 

# def divide(a,b):
#     c=a/b 
#     return c  

# print(add(2,3)) 
# print(subtract(10,5))
# print(multiply(1,6))
# print(divide(8,4)) 

# def create_name(first,last):
#     first=first.capitalize()
#     last=last.capitalize()
#     return first + " " + last 
# full_name=create_name("Anna", "Purna")
# print(full_name)

# Types of Arguments
# 1.positional 2.default 3.keyword 4.arbitrary

# Default Arguments = A defsult value for certain parameters.
                    # default is used when that argument is omitted 
                    # make your functions more flexible, reduces # of arguments

# def net_price(list_price,discount=0,tax=0.02):
#     return list_price * (1-discount) * (1+tax)
# print(net_price(400,0.1,0.03))
# print(net_price(400,0.2))
# print(net_price(400))

# import time 
# def count(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")
# count(50,45)

# keyword arguments = An argument preceded by an identifier helps with readability order of arguments doesn't matter

# def hello(greeting,title,first,last):
#     print(f"{greeting} {title} {first} {last}")
# hello("Hello", title="Ms.", last="Purna", first="Anna")

# "end" is an keyword
# for x in range(1,11):
#     print(x,end=" ")

#"sep" is an keyword
# print("1","2","3","4","5",sep="*")

# def get_phone(country,area,first,last):
#     return f"{country}-{area}-{first}-{last}"
# phone_num=get_phone(country=+91,area=824,first=779,last=4125)
# print(phone_num)

# Arbitrary Arguments = (*args) Allows you to pass multiple non-key arguments
#                       (**kwargs) Allows you to pass multiple keyword-arguments
#                        * unpacking operator

# def add(*args): 
#     total=0
#     for arg in args:
#         total+=arg
#     return total
#     # print(type(args)) --> tuple type
# print(add(2,3,7,5,4))

# def display_name(*args):
#     for arg in args:
#         print(arg,end=" ")
# display_name("Dr.","John","Doe","IIT")

# def print_address(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")
#     # print(type(kwargs)) --> Dictionary type
# print_address(street="Ambedhkar", city="Yeleswaram", state="AndhraPradesh", pin="533429")

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('apt-no')}")
    for key,value in kwargs.items():
        print(f"{key} : {value}")
shipping_label("Dr.","John","Doe","IIT",street="Ambedhkar",city="Yeleswaram",state="AP",code="533429")