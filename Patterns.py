# Pattern programs

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(n-i):
#          print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(i-1):
#         print(" ",end=" ")
#     for k in range(n+1-i):
#         print("*",end=" ")
#     print()

# n=int(input("Enter a number: "))
# for i in reversed(range(1,n+1)):
#     for j in range(i):
#         print("*",end=" ")
#     print()    

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()
# for i in reversed(range(1,n)):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()

# Number Patterns

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1, end=" ")
#     print()

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# n=int(input("Enter a number: "))
# num=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

# Alphabet Patterns

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(64+j+1),end=" ")
#     print()

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(64+i),end=" ")
#     print()

#Hollow patterns

# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1 or i==n or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

n=int(input("Enter a number: "))
for i in range(n):
    for j in range(2*n-1):
        if(i==0 or i==n-1 or j==0 or j==2*n-2 or i+j==n-1 or i-j==n-1+n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()