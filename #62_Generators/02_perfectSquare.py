
# Generators are a simple way to create iterators using functions. You can also

def topten():
    
    # This is a generator - it will return 5 and then pause the function
    
    n = 1 
    
    while n <= 10:
        sq = n*n
        yield sq
        n += 1
    
    




values = topten()
 
for i in values:
    print(i)
    
# why to use generators?
# - generators are easy to implement
# - generators are memory efficient
# - generators can be paused and resumed
# - useful in web scraping
# - useful in reading large files
# - useful in mathematical computations
# - useful in data streaming
