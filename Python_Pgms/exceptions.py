# EXCEPTIONS

try:
    file = open("file.py")
    age = int(input("Age : "))
    x = 100 / age
except (ValueError , ZeroDivisionError) as ex:
    print("enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("no exceptions")    
finally:            #always executed whether exception or not
    file.close()        #needed to release memory 


try:
    with open("file.py") as file:  #file is a obj.(var) which open func. returns
        print("File opened")
        
    age = int(input("Age : "))
    x = 100 / age
except (ValueError , ZeroDivisionError) as ex:
    print("enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("no exceptions")    
# with automatically releases,no need of finally



def spam(divideBy) : 
        return 42/divideBy
try:
        print(spam(2))
        print(spam('asd'))   
        print(spam(12))
        print(spam(0))
except TypeError:
        print('invalid value')
except ZeroDivisionError:
        print('cannot be 0')



# RAISING EXCEPTION
# don't raise it,as it reduces perf.

from timeit import timeit

code1 = """
def calc(age):
    if age <= 0:
        raise ValueError("age can't be zero")
    return 10/age

try:
    calc(-1)
except ValueError as err:
    pass
"""

code2 = """
def calc(age):
    if age <= 0:
        return None
    return 10/age


calc1 = calc(-1)
if calc1 == None:
    pass
"""
print("code1 = " , timeit(code1 , number=10000)) #no.of times code executes
print("code2 = " , timeit(code2 , number=10000))



 