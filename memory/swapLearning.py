# swap for immutable type : tuple , string , int 
# 对于immutable类,想要改变类的reference所指向的内容,只能让reference指向另外一个类.也就是指向的类的地址需要改变.

# 对于mutable类,可以直接通过修改reference的内容,因此可以将该reference传递到funciton中处,再fuction中,通过修改reference所指向的类的value,达到修改reference内容的目的.


## one without side effect

from typing import Tuple
from typing import List

def printDifference(s : str, var1 : any, var2 : any):
    print(str)
    print("var1: {} , id of var1 : {}".format(var1,id(var1)))
    print("var2: {} , id of var2 : {}".format(var2,id(var2)))

a , b = 1,2

print("Return value to assignment Before swap:")
print("a: {} , id of a : {}".format(a,id(a)))
print("b: {} , id of b : {}".format(b,id(b)))

'''
# x and y is the copied reference to a and b
# and the return value swap the referce 
# then assaignment the swaped  reference to a and b
# make the a refer to the old b object , meanwhile b refer to the old a object
'''
def swapTuple(x : int, y : int) -> Tuple[int]:
    return y,x

a , b = swapTuple(a,b)

print("Return value to assignment After swap:")
print("a: {} , id of a : {}".format(a,id(a)))
print("b: {} , id of b : {}".format(b,id(b)))

## another one with side effect
'''
# which means modified reference of outside scope from inside function 
# It use global keyword to let the variable's  scope change to inner side of  function
# Warning : in python , the name of object cannot being used without global keyword
# or it will promot error: local variable refered before assignment
'''

one = 1
two = 2

print("Global keyword value using Before swap:")
print("one: {} , id of one : {}".format(one,id(one)))
print("two: {} , id of two : {}".format(two,id(two)))

def swapTuple():
    global one , two 
    one , two = two , one

swapTuple()
print("Global keyword After swap:")
print("one: {} , id of one : {}".format(one,id(one)))
print("two: {} , id of two : {}".format(two,id(two)))

# mutable type swap
'''
It can be used as pointer of object in java
Change the content of pointer copied from parameter
Can change the variable at the same time
'''

def listSwap(i : List[any] , j : List[any]) -> List[any]:
    tmp = i[:]
    i[:]= j[:]
    j[:]= tmp[:]

listOne = ["My","name","is","john"]
listTwo = ["Hi","!"]
printDifference("List Before swap",listOne,listTwo)
listSwap(listOne,listTwo)
printDifference("List After swap",listOne,listTwo)