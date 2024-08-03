# 1) Take 10 names from the user and display the names that have length greater than 5.

x = int(input("Enter the number of elements: "))

list = []

for i in range(x) :
    list.append(str(input("Enter the element: ")))
    
# print(list)

def count(list):
    
    
    for i in list:
        if len(i) > 5 :
            print(i)
    


length = count(list) 






