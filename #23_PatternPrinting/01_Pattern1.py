# i = 1

# while i<=5:
#    print("# " , end="")
#    j = 1
#    while j <= 4:
#       print("# ",end="")
#       j = j+1   
#    i = i+1
#    print()

for i in range(4):        # represent No of rows
    for j in range(4):    # represent No of columns
     print("# ",end="")

    print()
    
'''
#
# #
# # #
# # # #'''
    


for i in range(4):        # represent No of columns
    for j in range(i+1):    # represent No of columns
     print("# ",end="")

    print()
    
    
'''
# # # #
# # #
# #
#
'''


for i in range(4):        # represent No of columns
    for j in range(4-i):    # represent No of columns
     print("# ",end="")

    print()
 