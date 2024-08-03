# zip() function is used to combine two lists into a single list of tuples

names = ("Aditya", "Divyanshu", "Lavish")
comps = ("nvidia", "intel", "amd", "apple", "google")

# zipped = list(zip(names, comps))
# zipped = dict(zip(names, comps))
zipped = zip(names, comps)

# print(zipped)

for (a,b) in zipped:
    print(a,b)
    
