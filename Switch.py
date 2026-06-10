# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                 Benefits: cleaner and syntax is more readable

# day_name=int(input("Enter a number of the day: "))
# def day_of_week(day):
#     if day==1:
#         return "It is sunday"
#     elif day==2:
#         return "It is Monday"
#     elif day==3:
#         return "It is Tuesday"
#     elif day==4:
#         return "It is Wednesday"
#     elif day==5:
#         return "It is Thursday"
#     elif day==6:
#         return "It is Friday"
#     elif day==7:
#         return "It is Saturday"
#     else:
#         return "Invalid day"
# print(day_of_week(day_name))

# Using match case statement
# day_name=int(input("Enter a number of the day: "))
# def day_of_week(day):
#     match day:
#         case 1:
#            return "It is sunday"
#         case 2:
#            return "It is Monday"
#         case 3:
#            return "It is Tuesday"
#         case 4:
#            return "It is Wednesday"
#         case 5:
#            return "It is Thursday"
#         case 6:
#            return "It is Friday"
#         case 7:
#            return "It is Saturday"
#         case _:
#            return "Invalid day"
# print(day_of_week(day_name))

# day_name=input("Enter a number of the day: ")
# def is_weekend(day):
#     match day:
#         case "Sunday":
#            return True
#         case "Monday":
#            return False
#         case "Tuesday":
#            return True
#         case "Wednesday":
#            return False
#         case "Thursday":
#            return True
#         case "Friday":
#            return False
#         case "Saturday":
#            return True
#         case _:
#            return False
# print(is_weekend(day_name))

day_name=input("Enter a day: ")
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
           return True
        case "Tuesday" | "Wednesday" | "Thursday" | "Friday" | "Saturday":
           return False 
        case _:
           return True 
print(is_weekend(day_name))