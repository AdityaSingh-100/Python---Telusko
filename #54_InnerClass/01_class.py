
class Student:
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() # Object of inner class
        
    def show(self): # self is a reference to the object of the class like - Student  
        print(self.name,self.rollno)
        self.lap.show()
        
    
    class Laptop: # Inner class - class inside a class 
        
        def __init__(self) :
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
            
        def show(self):
            print(self.brand,self.cpu,self.ram)
        
s1 = Student('Aditya',5)
s2 = Student('Rahul',6)


s1.show()
# s2.show() 

# # s1.lap.brand
# lap1 = s1.lap
# lap2 = s2.lap

# print(id(lap1))
# print(id(lap2))

# print(s1.name,s1.rollno)
# print(s2.name,s2.rollno)