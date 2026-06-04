# For Loops = Execute a block of code a fixed number of times. You can iterate over a range, string, sequence, ec..

# for x in reversed(range(1, 11,4)):
#     print(x)

# for x in range(1,21):
#     if x==15:
#         break
#     else:
#         print(x)

#Print even numbers from 1 to 20
# for x in range(1,21):
#     if x%2==0:
#         print(x)

#Print odd numbers from 1 to 20
# for x in range(1,21):
#     if x%2!=0:
#         print(x)

#Print sum of numbers from 1 to N
# n=int(input("Enter a number: "))
# sum=0
# for x in range(1,n+1):
#     sum+=x
# print(f"The total sum is: {sum}")

#Print Factorial of a number
# n=int(input("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"Factorial of a number is: {fact}")

#Multiplication of a table
# n=int(input("Enter a number: "))
# x=int(input("Enter a value for range: "))
# for i in range(1,x+1):
#     print(f"{n} x {i} = {n*i}")

#Count the number of digits in a number
# n=int(input("Enter a number: "))
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(f"The number of digits in a number is: {count}")

#Reverse of a number
# n=int(input("Enter a number: "))
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# print(f"Reverse of a number is: {rev}")

#Palindrome or not
# n=int(input("Enter a number: "))
# rev=0
# s=n
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if s==rev:
#     print(f"{s} is a palindrome..")
# else:
#     print(f"{s} is not a palindrome..")
