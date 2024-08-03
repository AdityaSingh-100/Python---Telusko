'''
map: Takes a function f, and a list L1, and returns a list L2 obtained by applying f to every element of L1. Say f is a function that takes x and returns 2x. Then, map(f, [1,2,3,4]) returns [2,4,6,8].

reduce: Takes a binary operator f, a list L and a seed value (or identity element). It returns the seed value if the list is empty. Otherwise, it applies the binary operator f to the seed and first element of L, then applies f to the result of this and the 2nd element of L, and so on till L is exhausted. The result is returned. This can be seen as a generalization of factorial function.

filter: Takes a boolean function f and a list L1. It applies the function to each element of L1, and list of those elements that give true is returned.
'''




#* filter function - filter(function, iterable) - returns an iterator were the items are filtered through a function to test if the item is accepted or not.

def is_even(n):
    return n % 2 == 0

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(is_even,nums))


print(evens)





#* filter With lambda function


nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n : n%2 == 0 ,nums))


print(evens) 



print("=====================================")



#* With Map function
#* Map function - map(function, iterable) - returns an iterator were the items are filtered through a function to test if the item is accepted or not.

def update(n):
    return n*2

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n : n%2 == 0 ,nums))

doubles = list(map(update,evens))

print(evens) 
print(doubles) 



print("Map function with lambda function")



nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n : n%2 == 0 ,nums))

doubles = list(map(lambda n : n*2,evens))

print(evens) 
print(doubles) 







print("=====================================")


#* With Reduce function - reduce(function, iterable) - returns a single value as a result of applying the function to the items of the iterable.

from functools import reduce

def add_all(a,b):
    return a+b

nums = [3,2,6,8,4,6,2,9]

# Reduce Function - reduce(function, iterable) - returns a single value as a result of applying the function to the items of the iterable.
evens = list(filter(lambda n : n%2 == 0 ,nums))

doubles = list(map(lambda n : n*2,evens))

sum = reduce(add_all ,doubles)

print(evens) 
print(doubles) 
print(sum)


print("Reduce function with lambda function")

from functools import reduce



nums = [3,2,6,8,4,6,2,9]

# Reduce Function - reduce(function, iterable) - returns a single value as a result of applying the function to the items of the iterable.
evens = list(filter(lambda n : n%2 == 0 ,nums))

doubles = list(map(lambda n : n*2,evens))

sum = reduce(lambda a,b : a+b ,doubles)

print(evens) 
print(doubles) 
print(sum)
