x = 2
print(x + 3)
y = 3
x + y
print(x+y)

x = 9
x + y
print(x+y)

# _ returns the value of the last executed expression value in Python Prompt/Interpreter

print(+ y) 

name = 'youtube'
print(name)

name + ' rocks!'
print(name + ' rocks!')

name[0]
print(name[0])
print(name[6])
#print(name[8])   IndexError: string index out of range
print(name[-1])
# -1 gives end letter of the string
print(name[-2])
# -2 gives second end letter of the string

# y o u t u b e
# 0 1 2 3 4 5 6  
print(name[-7])

print(name[0:2])
print(name[1:4])

print(name[1:])

print(name[3:10]) # it will not give any error and will print the string till the end

# name[0:3] = 'my' # TypeError: 'str' object does not support item assignment

# name[0] = 'R' # TypeError: 'str' object does not support item assignment

'my' + name[3:]
print('my' + name[3:])