 #*The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
class Computer:
    # pass # Empty class
    def __init__(self):
        self.name = "Aditya"
        self.age = 20
    
    def update(self): # self is a reference to the object itself 
        self.age = 30
       

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

c1.name = "Aditya"
c1.age = 20

if c1.compare(c2):
    print("Both are same")
else:
    print("They are different")

c1.update()

print(c1.name)
print(c2.name)




# print(id(c1))
# print(id(c2))