import math

x = math.sqrt(25)
print(x)

x = math.floor(2.9)
print(x)

x = math.ceil(2.2)
print(x)

x = math.pow(2, 3)
print(x)

x = math.pi
print(x)

x = math.e
print(x)

#NOTE - Math inside math 
x = math.floor(math.pi)
print(x)

import math as m
#NOTE - Making alias for math as m

x = m.sqrt(25)
print(x)

#NOTE - Importing only specific function from math
from math import sqrt,pow

print(pow(4,5))

#NOTE - help(math) will give all the functions available in math
help(math)
