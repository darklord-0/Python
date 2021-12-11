
letters = ['a','b','c']
for letter in range(len(letters)):
    print(letter , letters[letter])

for letter in enumerate(letters):
    print(letter , letter[0] , letter[1])  #  letter[0] accessing index 0 of resulting tuple from letter

# ex: items = [0, "a"] or (0, "a")
# index , letter = items  ; tuples can also be unpacked 

for index , letter in enumerate(letters):
    print(index , letter)

items = [
    ('P1' , 10),
    ('P2' , 30),
    ('P3' ,5),
] 
## SORTING LIST

# def sort_items(item): #here item is tuples in items
#     return item[1]
# items.sort(key=sort_items)
# print(items)

items.sort(key=lambda item : item[1]) 
print(items)# key= lambda parameters : expression


## MAPPING

# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices) 


# x = map(lambda item : item[1] , items) # map func returns an obj , which is iterable(can do looping to access)
# for item in x :
#     print(item)


prices = list(map(lambda item : item[1] , items)) # map func returns an obj , which is iterable(can do looping)
print(prices)

prices = [item[1] for item in items]    # LIST COMPREHENSION 
print(prices)

# FILTERING

filtered = list(filter(lambda item : item[1] >= 10 , items))
print(filtered)
    
filtered = [item for item in items if item[1] >= 10]
print(filtered)




