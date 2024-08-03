# 1) find fibonacci series till 50
# 0, 1 , 1 , 2 , 3 , 5 , 8

a=0
b=1

for i in range(0,50):
    print(a)
    c=a+b # c = 0+1 = 1
    a=b # a=1
    b=c # b=1
    if a>50:
        break
      
  
