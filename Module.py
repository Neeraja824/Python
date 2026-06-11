# Module = A file containing you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# print(help("modules"))
# print(help("math"))

# import math 
# print(math.pi)
# import math as m 
# print(m.pi)
# from math import pi 
# print(pi)
# from math import e 
# print(e)
# import math
# a,b,c,d,e=1,2,3,4,5
# print(e**a)
# print(e**b)
# print(e**c)
# print(e**d)
# print(e**e)

# print(math.e**a)
# print(math.e**b)
# print(math.e**c)
# print(math.e**d)
# print(math.e**e)

import ModuleExample
res1=ModuleExample.pi
res2=ModuleExample.square(5)
res3=ModuleExample.cube(7)
res4=ModuleExample.circumference(2)
res5=ModuleExample.area(4)
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)