# how can we check whether we use memory address we should not have allocated to

# id() sys.getrefcout()

'''
从经验来看,使用getrefcount()函数来查看,引用个数
最小的是应该是3
跟系统默认的引用有关,加上getrefcount()函数的形参,也会占用一个引用个数
另外一个引用,目前还不太清楚
'''
import sys
from typing import Tuple
# import type

# str1 = str2 = "hi!"
# str1  = "hi!"
# idOfStr = id(str1)
# count = sys.getrefcount(str1)
# countCount = sys.getrefcount(count)

# print("the type of variable 'count' is {}, with value {} in address {}.And the refer to count is {}".format(type(count),count,idOfStr,countCount))

# str1 = "hello!"
# count = sys.getrefcount(str1)
# print("refer to str1 is : {}".format(sys.getrefcount(str1)))
# idOfStr = id(str1)
# print(sys.getrefcount("hello"))

x = 2
y = 3
def swap(a : int, b : int) -> Tuple[int,int]:
    tmp = a
    a = b
    b = tmp
    #return (a,b)
    return a,b

print("x: {0[0]} \ny: {0[1]} \ngreeding: {1[0]}".format(swap(x,y),("hi","hello")))
print(type(swap(x,y)))