# Logical Operator

#OR operator
temp=25
is_raining=False
if temp>35 or temp<0 or is_raining:
    print("The outdoor event is cancelled..")
else:
    print("The outdoor event is still scheduled..")

#AND operator
temperature=25
is_sunny=True

if temperature >= 28 and is_sunny:
    print("It is sunny🌞")
else:
    print("It is cloudy☔")

#NOT Operator
num1=0
num2=1
if num1==0 and num2==1:
    print("Both are same..")
elif num1==0 and not num2==0:
    print("Both are not equal..")
else:
    print("❤️❤️")

##  Terenary Operators -> x if condition else y
## A one-line shortcut for the if-else statement print or assign one of two values based on a condition

num=45
res="Even" if num%2==0 else "ODD"
print(res)

#Maximum of numbers
a=8
b=3
max_num = a if a>b else b
print(max_num)

#Minimum of numbers
x=7
y=4
min_num=x if x<y else y
print(min_num)

#Adult or not
age=53
status="Adult" if age>=18 else "Child"
print(status)

#Temperature based condition
temper=35
weather="Hot" if temper>30 else "Cold"
print(weather)