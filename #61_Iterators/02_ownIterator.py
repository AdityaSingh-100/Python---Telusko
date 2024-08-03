

class TopTen:
    
    
    def __init__(self):
        self.num = 1
        
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.num <=10:
            val = self.num
            self.num += 1
            
            return val # return the value of the iterator
        
        else:
            raise StopIteration # raise StopIteration exception when the iteration is done
    
    
values = TopTen()


print(next(values))


for i in values:
    print(i)
    
    
    
# for i in values:
#     print(i)

# print(values.__next__())

# print(values.__next__())