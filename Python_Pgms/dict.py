# DICTIONARY
# keys must be immutable type(strings,numbers,) only whereas val can be anything

point = {"x" : 1 , "y" : 2 }
point1 = dict(x = 1 , y = 2) #must pass 1 or more keyword arg.
print(point1["x"])  #can't access with numeric index
point1["z"] = 30    #adding new key
print(point1.get( "a" , 0 ))    #checking if present 'a',and returning default val
del point1['x']

print(point1)

#iterating over dict.
for key in point1:
    print(key, point1[key])

for x in point1.items():
    print(x)        #returns tuples

for key , value in point1.items():      #unpacking beforehand
    print(key , value)

#DICTIONARY COMPREHENSIONS(for list,set,dict,tuples)
values = {}
for x in range(5):
    values[x] = x * 2
print(values)


values = { x : x * 2 for x in range(5) }
print(values)
for x in values:
    print(x , values[x])
