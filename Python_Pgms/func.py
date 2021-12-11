

list1 = [1,2,3]
list2 = [10,20,30]

print(list(zip(list1 , list2)))
print(list(zip("abc" , list1 , list2)))

#   TUPLES

point = 1,2 #acts as a tuple even without paranthese
print(type(point))
point1 = 1, #must hv a trailing comma for it to be a tuple
print(point + point1 )

#tuple func takes any iterable arg.(here list,string)  
list3 = tuple([1 , 2] * 2) #to convert a list to tuple
print(list3)

print(tuple("hello"))


#SWAPPING 
x = 10
y = 20
# on R.H.S. we defining a tuple and unpacking it on L.H.s.
x , y  = y , x
print(f"x : {x} y : {y} ")

#ARRAYS
from array import array
num = array("i" , [1,2,3])
print(num.append(56)) #can do all prev. methods
# here we can't modify array if given value of diff. type
## ex : num[0] = 1.0  


# SETS
num = [1,2,1,7,5,2]
num2 = set(num) #unordered collection of uniques
num1 = {1,5}
num1.add(8)

print(f"num1 : {num1} ")
print(f"num2 :  {num2} ")
print(num1 | num2) #UNION
print(num1 & num2) #INTERSECTION
print(num1 - num2) #DIFFERENCE
print(num1 ^ num2) #SYMMETRIC DIFF

#since set is unordered we can't access items with indexing