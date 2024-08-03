#NOTE 1 - datatype in Python : None,Numeric,List,Tuple,Set,String,Range,Dictionary

'''Numeric: int,float,complex,bool'''
num = 2.5
print(type(num))

num = 5
print(type(num))

num = 6 + 9j
print(type(num))

#NOTE - Convert into other datatype

a = 5.6
b = int(a)
print(type(a))
print(type(b))

print(5)

k = float(b)
print(k)

k = 6
c = complex(b,k)
print(c)


# Boolean
print(b<k)
bool = b<k
print(bool)
print(type(bool))

print(b>k)

print(int(True))
print(int(False))



'''List,Set,Tuple,String,Range'''
List = [25,36,45,12]
print(List)
print(type(List))

s = {34,53,12,53,23}
print(s)
print(type(s))

t = (23,43,5,21,64,12)
print(t)
print(type(t))

str = "Aditya"
print(type(str))

#NOTE - Range
range(10)
print(range(10))

# to view this range in list format just use this --  list(range(10))
list(range(0,10)) # callable error always name them different to fix this error
print(list(range(0,10)))

list(range(2,10,2)) # 2 - start , 10 - end , difference - 2
print(list(range(2,10,2)))

print(type(range(10)))

#ANCHOR - Keys should be uniques values can
d = {'navin':'samsung','rahul':'Iphone','Aditya': 'Oneplus'}
print(d)

print(d['rahul'])

print(d.get('Aditya'))