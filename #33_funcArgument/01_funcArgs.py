
def update(x):
    
    print(id(x))
    
    x = 8
    print(id(x))
    print("x",x)
    
    

a = 10
print(id(a))
update(a)
print("a",a)

# Call by value - Python does not support call by value
# Call by reference - Python does not support call by reference
print()
print()




def update2(x):
    
    print(id(x))
    
    lst[1] = 25
    print(id(lst))
    print("lst",lst)
    
    

lst = [10,20,30]
print(id(lst))
update2(lst)
print("lst",lst)
