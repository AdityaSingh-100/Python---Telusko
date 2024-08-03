# instance variable: variable inside the constructor 
# the variable inside init becomes instance variable

# class variable: variable outside the constructor
# the variable outside init and inside class becomes class variable
 


class Car:
    
    wheels = 4 # ---> class variable
    
    def __init__(self) :
        self.mil = 10 # ---> instance variable
        self.com = "Audi" # ---> instance variable
        
        

        
#* Namespaces: namespace is an are where you create and store object/variable
#* 1. class namespace - class variable
#* 2. object/instance namespace - instance variable
        
        
c1 = Car()
c2 = Car()

c1.mil = 8



print(c1.com, c1.mil,c1.wheels)
print(c2.com, c2.mil,c2.wheels)