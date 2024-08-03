# init method/function is a constructor in python which is used to initialize the object of a class. 

class Computer:
    
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        print("In init method")
        
    def config(self):
        print("Config is :",self.cpu, self.ram) # self is a reference to object  
        
        
        
comp1 = Computer('i5',16) # object creation
comp2 = Computer('ryzen 7',8) # object creation

# comp1.config() # calling method of class
comp2.config() # calling method of class