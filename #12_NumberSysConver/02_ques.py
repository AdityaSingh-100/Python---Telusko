# Find binary representation of a decimal number
# 31 , 52 , 65 

print(bin(31))
print(bin(52))
print(bin(65))

# Find binary representation of a decimal number
# 31 , 52 , 65
# ob11111, 0b110100, 0b1000001

print((0b11111))
print((0b110100))
print((0b1000001))  

# Question

a = 15
b = 12

x = (a //4 + b**3) < 2000 and (b%4  != 0)

#  floor division operator // rounds the result down to the nearest whole number 
#  15//4 = 3
#  12**3 = 1728 so total = 1731
#  1731 < 2000 is True
#  12%4 = 0 so b%4 != 0 is False
#  True and False = False
print(x)