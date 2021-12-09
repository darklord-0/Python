for x in range(10):
    print(x * 2)


# COMPREHENSIONS
#list
values = [x*2 for x in range(10)]
print(values)   #here values is a list
for x in values:    #we are iterating over it to get each value
    print(x)

#set
values = {x*2 for x in range(10)}
print(values)
for x in values:
    print(x)

#tuple
values = (x*2 for x in range(10))
print(values)
for x in values:
    print(x) 

# generator obj. are iterable,don't store all values in memory
# since don't store all items in memory , we can't use len(values)
from sys import getsizeof
values = (x*2 for x in range(10000))
print(f"gen : {getsizeof(values)} bytes ")

values = [x*2 for x in range(10000)]
print(f"list : {getsizeof(values)} bytes ")



