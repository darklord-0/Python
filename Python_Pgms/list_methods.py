
num = [5,3,6,2,7,5,3]
num2 = num.copy()

num.append(10)                   #IN ALL THIS ORIGINAL IS NOT CHANGED
num.insert(0,20)
num.remove(7) #only rem first occurence
num.pop()
num.pop(2) # only used for one item
# num.clear()
del num[4]
del num[0:3] # del can be used for range of items
print(num.index(5))
print(6 in num)
print(num.count(5))

num2.sort() #sort() changes our original list 
num2.reverse() # or num.sort(reverse = True)
print(sorted(num2 , reverse = True)) # it doesn't changes our original list
print(num2)
print(num)

num3 = []       #to remove duplicates
for n in num2:
    if n not in num3:
        num3.append(n)
print(num3)


# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for i in supplies:
#      print('supplies is: ' + i )

# for j in range(len(supplies)):      #prefer to use this technique
#     print(f'index {j} in supplies is : {supplies[j]}')  