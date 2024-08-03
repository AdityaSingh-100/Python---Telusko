
class A:
    
    def __init__(self): # self - instance of class A is passed to constructor of class A 
        print("In A init")
    
    
    def feature1(self):
        print("Feature 1 working")
        
    
    def feature2(self):
        print("Feature 2 working")
        
        
class B(A): # Inheriting class A
    
    def __init__(self):
        super().__init__() # super() is used to call constructor of parent class
        print("In B init")
    
    def feature3(self):
        print("Feature 3 working")
        
    
    def feature4(self):
        print("Feature 4 working")
        
        
a1 = B() # here B is constructor and it will call A's constructor

'''
subclass = child class(B)
superclass = parent class(A)
If we try to create object of sub class it will first try to find constructor in sub class, if not found then it will go to parent class and find constructor in parent class.

#NOTE - when you create object os sub class it will call init of sub class first and if you have call super then it will first call init of super class then call init of sub class
'''