
# key word arguments - **kwargs - double star operator is used to pass the key word arguments in the function

def person(name, **data):
    
    print(name)
    print(data)   
    
    
    for i,j in data.items(): # items() is used to get the key value pair
        print(i,j)
 
 

        
person('Aditya',age = 20,city = 'Karauli',mob = 9865432)