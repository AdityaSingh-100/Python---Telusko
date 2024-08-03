''' Bitwise Operator
1. Bitwise AND(&)
2. Bitwise OR(|)
3. Bitwise XOR(^)
4. Bitwise NOT/Complement(~)
5. Bitwise Left Shift(<<)
6. Bitwise Right Shift(>>)

'''

# Not
~12
print(~12) # -13 it computes the 2's complement of the number and then gives the value of the number in negative. 

# And
print(12 & 13) # 12 - eg. 1100 & 1101 = 1100

# Or
print(12 | 13) # 13 - eg. 1100 | 1101 = 1101

print(25 & 30) # 24 - eg. 11001 & 11110 = 11000

# XOR
print(12 ^ 13) # 1 - eg. 1100 ^ 1101 = 0001


#eg
print(25^30) # 7 - eg. 11001 ^ 11110 = 00111

# Left Shift
print(10 << 2) # 40 - eg. 1010 << 2 = 101000

# Right Shift
print(10 >> 2) # 2 - eg. 1010 >> 2 = 10  

# In left shift, the bits are shifted to the left by the number of positions specified. Gaining the value of the number.
# In right shift, the bits are shifted to the right by the number of positions specified. Losing the value of the number.