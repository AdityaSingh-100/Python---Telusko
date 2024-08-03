from numpy import *

m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('1 2 3; 4 5 6; 2 3 9')

m3 = m1 + m2

print(m3)

m3 = m1 * m2

print(m3)