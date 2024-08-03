# Duck Typing - If it looks like a duck, swims like a duck and quacks like a duck, then it probably is a duck.
# In Python, we don't care about the type of object, we only care about the behavior of the object.


class PyCharm:
    
    def execute(self):
        print("Compiling")
        print("Running")

class Vscode:
        
        def execute(self):
            print("Spell Check")
            print("Convention Check")
            print("Compiling")
            print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()
        
# ide = PyCharm()
ide = Vscode() # creating object of MyEditor class(ide)
        
lap1 = Laptop()
lap1.code(ide)