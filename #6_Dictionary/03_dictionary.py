#NOTE 1. Dictionary is a collection of key-value pairs.
data = {1:'Aditya',2:'Eren',4:'vegeta',3:'Goku'}
print(data)


print(data[1])
print(data[3])



# NOTE 2. Dictionary is mutable
data.get(1)
print(data.get(1))

print(data.get(5)) # NOTE Print None

print(data.get(5,'Not Found')) # NOTE Print Not Found

print(data.get(3,'Not Found')) # NOTE Print Goku

keys = ['Aditya','Eren','vegeta','Goku']
values = ['Python','CPP','C#','Java']

data = dict(zip(keys,values))
print(data)



#NOTE 3
print(data['Eren'])

#FIXME -  print(data['Monika']) # NOTE Error

data['Monika'] = 'JavaScript'
print(data)

#NOTE 4 to delete value
del data['Monika']

print(data)



#NOTE 5 - dictionary inside dictionary

prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(prog)

print(prog['JS'])
print(prog['Python'])
print(prog['Python'][1])
print(prog['Python'][0])


print(prog['Java'])
print(prog['Java']['JEE'])