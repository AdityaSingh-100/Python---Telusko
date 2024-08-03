a = 5
b = 6

#1 Using Third Variable or Temporary variable
temp = a
a = b
b = temp

print(a)
print(b)

#2 Without using Third Variable

a = a + b # 11
b = a - b # 5
a = a - b # 6

print(a)
print(b)

#3 Using XOR
a = 2 # 101 bit
b = 3  # 110 bit

# XOR is used to swap the bits without wasting the bits

a = a ^ b # 011
b = a ^ b # 101
a = a ^ b # 110
print(a)
print(b)

#4 Using ROT_WOT() a,b goes in stack and comes out in reverse order or swaps the two top most stack items
a= 7
b=8
a,b = b,a
print(a)   
print(b)