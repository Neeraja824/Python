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
num=45
res="Even" if num%2==0 else "ODD"
print(res)