dict = {'a':1, 'b':2, 'c':3}
print(type(dict))

# print value of a particular key
value = dict['a']
print('value of key a is %6s' %value)

# print values in dictionary
for i in dict.values():
    print('value in dictionary is :%5s' %i)


# print keys in dictionary
print("keys in dictionary are:")
for i in dict.keys():
    print(i)


# print key/value pair in dictionary
j,k = (1,2)
t = type((j,k))
print("type of j,k is: %30s" %t)
print("keys/values in dictionary are:")
for j,k in dict.items():
    print(j,k)

# seperate value can join into a tuple
i = 'a'
j = 1
print(i,j)
