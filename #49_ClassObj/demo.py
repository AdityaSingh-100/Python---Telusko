
class Computer: # class creation
    
    def config(self):
        print("ryzen 7", "16gb", "512ssd")


# class is a blueprint of object
# object is an instance of class
# x = 9 
# print(type(x)) 

# a = '8'
# print(type(a))

comp1 = Computer() # object creation 
comp2 = Computer() # object creation

Computer.config(comp1) # calling method of class
Computer.config(comp2) # calling method of class

# OR

comp1.config() # calling method of class
comp2.config() # calling method of class
# print(type(comp1))

a = 5
a.bit_length()