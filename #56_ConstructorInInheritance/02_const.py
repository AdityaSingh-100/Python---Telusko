#REVIEW - How constructor behaves in inheritance
#REVIEW - How to use super() in Inheritance
#REVIEW - MRO - Method Resolution Order

class A:
    
    def __init__(self): # self - instance of class A is passed to constructor of class A 
        print("In A init")
    
    
    def feature1(self):
        print("Feature 1-A working")
        
    
    def feature2(self):
        print("Feature 2 working")
        
        
class B(): 
    
    def __init__(self):
        print("In B init")
    
    def feature3(self):
        print("Feature 1-B working")
        
    
    def feature4(self):
        print("Feature 4 working")
        
class C(A,B):
    def __init__(self):
        super().__init__() # super() is used to call constructor of parent class
        print("In C init")
        
        
    def feat(self):
        super().feature2() # super() is used to call method of parent class
        
#* MRO - Method Resolution Order - It will first find constructor in class C, if not found then it will go to class A and then class B - Left to Right
        
a1 = C() # here B is constructor and it will call A's constructor
a1.feat()

# To represent super class we use super() method











'''
subclass = child class(B)
superclass = parent class(A)
If we try to create object of sub class it will first try to find constructor in sub class, if not found then it will go to parent class and find constructor in parent class.

#NOTE - when you create object os sub class it will call init of sub class first and if you have call super then it will first call init of super class then call init of sub class
'''