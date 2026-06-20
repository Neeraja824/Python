# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class child(parent)

# Single Inheritance

# class Animal:
#     def __init__(self,name):
#         self.name=name
#         self.is_alive=True

#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     def speak(self):
#         print("Bow Bow Bowwww!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow Meow Meowww!")

# class Mouse(Animal):
#     def speak(self):
#         print("Kich Kich Kichhhh!")

# dog=Dog("Leo")
# cat=Cat("Chiru")
# mouse=Mouse("Micky")

# print(dog.name)
# print(dog.is_alive)

# dog.eat()
# dog.sleep()
# dog.speak()

# cat.speak()
# mouse.speak()

# Multiple Inheritance = inherit from more than one parent class
# Multi-level Inheritance  = inherit from a parent which inherits from another parent

class Animal:
    def __init__(self,name):
        self.name=name
    
    def eat(self):
        print(f"This {self.name} is eating")
    
    def sleep(self):
        print(f"This {self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is fleek!")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit=Rabbit("Bugs")
hawk=Hawk("Tony")
fish=Fish("Nemo")

rabbit.flee()
rabbit.eat()
rabbit.sleep()
