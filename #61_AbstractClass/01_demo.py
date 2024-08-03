from abc import ABC, abstractmethod

class Computer:
    @abstractmethod
    def process(self):
        pass     # Abstract method - no implementation provided(no declaration)
    
    
class Laptop(Computer):
    #    pass
        # If we don't provide the implementation of process() method in Laptop class
        # then it will give an error. 
        # TypeError: Can't instantiate abstract class Laptop with abstract methods process
        
        def process(self):
            print("Its running")



class Whiteboard(Computer):
    def write(self):
        print("Writing")



class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()
        
        
        
# com = Computer()
com1 = Laptop()
# com.process()
com2 = Whiteboard()

prog1 = Programmer()

prog1.work(com2)
        
com1.process()


'''

Summary:
abstract method is a method which only has declaration and doesn't have definition.
a class is called abstract class only if it has at least one abstract method.
when you inherit a abstract class as a parent to the child class, the child class should define all the abstract method present in parent class.
if it is not done then child class also becomes abstract class automatically.
at last, python by default doesn't support abstract class and abstract method, so there is a package called ABC(abstract base classes) by which we can make a class or method abstract



I see many are still confused with the concept and also with "how is it different from duck typing". Here is an example to get it cleared. 

This is an exam 'hall' and there are students from 2 diffrent 'classes' seated. Class A has a maths test, Class B has social.

The invigilator says that to enter the hall, every one must carry an instrument box. Now students of classes both A and B must bring one even if B class don't have its use. So the class A will have a set of compass, rulers, pencils etc in it. But since students of class B don't have any use, they will just bring one with a pencil or even just empty (pass) because its compulsory to bring one in to be in the hall.

If a parent class has an abstract method, every child must also have one. So each child will have to define one of thier own.

In duck typing, It isn't necessary to define the parent class method for each child classes. it just simply have to point to the class where the particular method lies. Here we would have to define for each.
'''