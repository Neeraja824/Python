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

#Sum of even numbers from 1 to N
# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum+=i
# print(f"The sum of even numbers is: {sum}")

#Sum of odd numbers from 1 to N
# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     if i%2!=0:
#         sum+=i
# print(f"The sum of even numbers is: {sum}")

#Find the largest digit in a number.
# a=float(input("Enter a first number: "))
# b=float(input("Enter a second number: "))
# c=float(input("Enter a third number: "))
# max_num=max(a,b,c)
# print(f"The largest number is: {max_num}")

# Check whether a number is an Armstrong number.
# n=int(input("Enter a number: "))
# temp=n
# digits=len(str(n))
# sum=0
# for digit in str(n):
#     sum+=int(digit)**digits
# if sum==n:
#     print(f"{n} is an Armstrong number")
# else:
#     print(f"{n} is not an Armstrong number")

#Check whether a number is a Strong number.
# n = int(input("Enter a number: "))
# temp = n
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
#     sum += fact
#     temp //= 10
# if sum == n:
#     print(f"{n} is a Strong Number")
# else:
#     print(f"{n} is not a Strong Number")

#Print all factors of a number.
# n=int(input("Enter a number: "))
# print(f"Factors of the given number are: ")
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

#Check whether a number is prime.
# n=int(input("Enter a number: "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

#Print all prime numbers between 1 and N.
n = int(input("Enter a number: "))
for num in range(2, n + 1):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num, end=" ")