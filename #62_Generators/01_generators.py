
# Generators are a simple way to create iterators using functions. You can also

def topten():
    
    yield 1 # This is a generator - it will return 5 and then pause the function
    yield 2
    yield 3
    yield 4
    
    
    




values = topten()
 
print(values.__next__()) # give us a generator object
print(values.__next__())

for i in values:
    print(i)