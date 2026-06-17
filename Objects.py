# Object = A bundle of related attributes (variables) and methods (functions)
# Ex. phone,cup,book
# You need a class to create many objects

# Class = It is an blueprint used to design the structure and layout of an object

# from car import Car
# car1=Car("Mustang",2024,"red",False)
# car2=Car("BMW",2025,"blue",True)
# car3=Car("Audi",2023,"black",True)

# # car1.drive()
# # car2.stop()
# car1.describe()

# print(car3.model)
# print(car3.year)
# print(car3.color)
# print(car3.for_sale)

# Class Variables = A shared among all instances of a class
#                   It defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    class_year=2025
    num_students=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_students+=1

student1=Student("Aditya",21)
student2=Student("Neeru",20)
student3=Student("Uma",19)
student4=Student("Anu",38)

# print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
# print(student1.name)
# print(student1.age)
# print(Student.class_year)