# name=input("Enter your name: ")
# #Length function -> count the length of the word
# print(len(name))

# #find function -> count a first occurence of a word
# print(name.find(" "))

# #rfind function -> count a last occurence of a word
# print(name.rfind(" "))

# #Capitalize the first letter of a word
# print(name.capitalize())

# #Uppercase the all letters of a word
# print(name.upper())

# #Lowercase the all letters of a word
# print(name.lower())

# #It contains only numbers not any alphabets
# print(name.isdigit())

# #It contains only alphabets not any numbers
# print(name.isalpha())

# #Count the "-" in a phone number
# phone_number=input("Enter your phone number: ")
# phone_num=phone_number.count("-")
# print(phone_num)

# #replace the "-" with the any other symbol
# phone=input("Enter your number: ")
# print(phone.replace("-" , "*"))

# print(help(str))

#Username is no more than 12 characters
#Username must not contain spaces
#Username must not contain digits
username=input("Enter a username: ")
if len(username) > 12:
    print("Your username can't be more than 12 characters..")
elif not username.find(" ")== -1:
    print("Your username can't contain spaces..")
elif not username.isalpha():
    print("Your username can't contain numbers..")
else:
    print(f"Welcome {username}")
