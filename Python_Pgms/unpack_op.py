#  UNPACKING OPERATOR
# to take out value in any iterable

#list
num = [12,34,56,78,93]
first , sec , *other = num  # we are unpacking the list into the variables
print(first , sec)          # and packing the rest nums in 'other'
print(other) 


num1 = [1,2,3]
num2 = [4,6]
print(num1)
print(*num1)    


print(*range(5)) 
print([*range(5) , *"hello" ,*num2  ]) #unpacking numbers and strings and putting in list


#dictionary

first = dict(x = 1 , y = 3)
sec = dict( y = 22 )
print({**first , **sec , "z" : 5 })