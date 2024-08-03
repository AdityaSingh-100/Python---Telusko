


class Student:

    school = 'Telusko'
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):   # ---> instance method because it is taking self as argument
        return (self.m1 + self.m2 + self.m3)/3
            
    @classmethod  # --> decorator
    def getSchool(cls): # class method because it is taking cls as argument
        return cls.school
    
    @staticmethod # --> decorator 
    def info():
        print("This is Student class... in abc module")
    
        
    
        
s1 = Student(34,62,32)
s2 = Student(89,32,12)


print(s1.avg())
print(s2.avg())
# print(Student.info())

Student.info()

'''
Types of Instance Methods:
    - Instance Method
    - Class Method
    - Static Method
    - Abstract Method
    - Property Method
    - Accessor Method - to access the value
    - Mutator Method - to modify the value
'''

'''
Accessor Method: 
    - method which is used to access the instance variable
    - it is also called as getter method
    - it is used to get the value of the instance variable
    - it is used to read the value of the instance variable
    - it is used to access the value of the instance variable
    
Mutator Method:
    - method which is used to modify the instance variable
    - it is also called as setter method
    - it is used to set the value of the instance variable
    - it is used to modify the value of the instance variable
    - it is used to change the value of the instance variable
'''


