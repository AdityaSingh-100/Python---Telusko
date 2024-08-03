
av = 10
x = int(input("How many candies you want"))

i = 1
while i <= x:
    
    if i > av:
        print("Out of stock")
        break
    print("Candies")
    i +=1

print("Bye")

'''

Break : to end the loop. It uses with if statement to put a condition so you can break the loop and exit. 

Continue : to skip the remaining code of the loop when a certain condition happen (like in if statement), but still looping. 

Pass: uses for impty blocks when you don't have a code to write.'''