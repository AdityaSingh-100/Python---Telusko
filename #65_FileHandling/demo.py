
#  f = open(r'D:\1.Coding\PYTHON\Python-Telusko\#65_FileHandling\MyData.txt') #absolute path
f = open('MyData.txt','r') #absolute path
 # we need to provide absolute path of the file because our coding file 
 # and the file we are trying to access are in different directories


# print(f.read())
 # print(f.readline(),end="") 
 # print(f.readline(4),end="")
 # print(f.readline())

# f1 = open('abc','w')



#  for abc file

# f1 = open('abc','w') # w - write into file
# f1 = open('abc','a') # a - append into file

# f1.write("Something")
# f1.write("\nPeople")
# f1.write("Mobile")


# Read all data from MyData.txt and write it into abc file

# for data in f:
#     f1.write(data)

f = open('img1.JPG','rb') #rb - read binary

f1 = open('MyPic.JPG','wb') #wb - write binary


for i in f:
    # print(i)
    f1.write(i)
    