# Variable scope = Where a variable is visible and accessible 
# Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# 1.Local Scope (L)
# A local scope is the scope inside a function. 
# Variables defined within a function can only be accessed inside that function.
def show():
    x=10
    print(x)
show()

# 2. Enclosing Scope
# An enclosing scope is the scope of an outer function that contains a nested (inner) function.
# Variables of the outer function can be accessed by the inner function.
def outer():
    x=20
    def inner():
        print(x)
    inner()
outer()

# 3. Global Scope
# A global scope is the scope of variables defined outside all functions.
# These variables can be accessed throughout the program.
x=30
def fun():
    print(x)
fun()

# 4. Built-in Scope
# A built-in scope contains names that are pre-defined by python,
# such as built-in functions and exceptions.
numbers=[1,2,3,4,5]
print(len(numbers))
print(max(numbers))
print(min(numbers))