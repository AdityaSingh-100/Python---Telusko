
class A:
    def feature1(self):
        print("Feature 1 working")
        
    
    def feature2(self):
        print("Feature 2 working")
        
        
class B(A): # Inheriting class A
    def feature3(self):
        print("Feature 3 working")
        
    
    def feature4(self):
        print("Feature 4 working")
        
        
class C(B): # Inheriting class B
    def feature5(self):
        print("Feature 5 working")
        
    
        
a1 = A() # A is constructor
a1.feature1()
a1.feature2()


b1 = B()
b1.feature1()

c1 = C()
c1.feature4() # Feature 4 working