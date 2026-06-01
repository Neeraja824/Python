# Addition Operator
num1=10
num1+=5
print(num1)
#Subtraction Operator
num2=10
num2-=5
print(num2)
#Multiplication Operator
num3=10
num3*=5
print(num3)
#Divison Operator
num4=10
num4/=5
print(num4)
#Exponent Operator
num5=10
num5**=5
print(num5)
#Modulo Operator
num6=10
num6%=5
print(num6)


#Basic Functions
x=3.14
y=-4
z=5
res=round(x)
res1=abs(y)
res2=pow(4,3)
res3=max(x,y,z)
res4=min(x,y,z)
print(res)
print(res1)
print(res2)
print(res3)
print(res4)

#Math Function
import math
x=9.1
print(math.pi)
print(math.e)
result=math.sqrt(x)
result1=math.ceil(x)
result2=math.floor(x)
print(result)
print(result1)
print(result2)

#Circumference of a circle
radius=float(input("Enter the radius of a circle: "))
circum=2*math.pi*radius
print(f"The circumference of a circle is: {round(circum,2)}cm")

#Area of a circle
r=float(input("Enter the radius of a circle: "))
area=math.pi*pow(r,2)
print(f"The area of the circle is: {round(area,2)}cm")

#Pythagoras Theorem
a=float(input("Enter the side A: "))
b=float(input("Enter the side B: "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"The value of the c is: {c}")