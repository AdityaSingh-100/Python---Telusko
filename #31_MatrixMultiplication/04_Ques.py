# 1 write a code to multiply two matrices using 2D array and using loops
from numpy import *

m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('1 2 3; 4 5 6; 2 3 9')

m3 = m1 * m2

print(m3) 

result = 1

for i in range(2):
    for j in range(2):
        for k in range(3):
            result[i][j] += m1[i][k] * m2[k][j]
            
print(result)