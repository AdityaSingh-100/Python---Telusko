
x = int(input("Enter the number of elements: "))

list = []
for i in range(x):
    list.append(int(input("Enter the element: ")))


def count(list):
    
    even = 0
    odd = 0
    
    for i in list:
        if i % 2 == 0 :
            even += 1
        else:
            odd += 1
        
    return even,odd



even, odd = count(list) 

print("Even: {} and Odd: {}".format(even, odd))  # format() method is used to format the output in a specific way.

