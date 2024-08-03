#1. What is the output of the following code?
x = bin(7<<2)
print(x) # 11100
print(bin(7)) # 111

#2 What is the output of the following code?
#125 | 265
# 125 = 1111101
# 265 = 100001001
print(125 | 265) # 381
print(bin(381))

#3 What is the output of the following code?
# 652 ^ 125
# 652 = 1010001100
# 125 = 1111101
print(652 ^ 125) # 753  

#4 What is the output of the following code?
(288 << 2) >> (26 // 6)
288 << 2 # 1152 - in binary 0b100100000
26 // 6 # 4
print(288 << 2) # 1152
print(bin(288))

print(bin(1152))

print((288 << 2) >> (26 // 6)) # 1152 >> 4 = 72