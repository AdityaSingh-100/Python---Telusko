# NOTE - Overiding is a concept of OOPs where a method of parent class is redefined in the child class.
#* Popularly known as Overiding.Used in various software development projects.

class A:
    
    def show(self):
        print("In A Show")
        
        

class B(A):
    print("In B Show")
    # pass
    
    
        

a1 = B()
a1.show()