from decimal import localcontext,Decimal,ROUND_HALF_UP
# str
spam = input('EveryThing you input is string: ')

# convert str to int if possible
print(int(spam))

# float
# float() will returen a float point number with only one decimal
print(float(spam))

# convert int to binarry code
baseTenInt = int(spam)
binaRray = []

## loop for division by 2
## remainder is the index by that power
## if remainder is zero , then power of that level is zero
while(( baseTenInt   )!= 0):
    codeInBit = baseTenInt % 2
    # if(codeInBit == 0):
    #     binaRray.insert(0,0)
    # else:
    #     binaRray.append(0,1)
    binaRray.insert(0,codeInBit)
    baseTenInt = baseTenInt // 2

index = 0
for i in binaRray:
    print(str( index  )+ " : " + str( i ) )
    index+=1

print("binarry is: ")
print(binaRray)

## round function for floating point number
## python默认的round规则是,趋向于最近的整数,如果距离相同,则趋向于偶数
## Python uses IEEE 754 rounding rules(https://en.wikipedia.org/w/index.php?title=IEEE_754#Rounding_rules)
# 在以下例子中,如果以10的0次方,也就是1的倍数作为趋近对象.也就是0,1,2,3...9
# 那么如果存在0.5,则会趋近与0,2,4,6,8
# 如果以10的-1次方,也就是0.1作为趋近对象,那么猜测应该以0.2,0.4,0.6,0.8为趋近对象
for i in range(1,15,2):
    floatNumber = i / 2
    rounderNumber = round(floatNumber)
    print(str(floatNumber) + " -> " + str( rounderNumber ))

for i in range(1,15,2):
    floatNumber = i / 4
    rounderNumber = round(floatNumber,1)
    print(str(floatNumber) + " -> " + str(rounderNumber))

# 如果想要实现4舍5入的效果,那么可以通过Decimal这个module来实现
# https://docs.python.org/3/library/decimal.html
'''
from decimal import localcontext,Decimal,ROUND_HALF_UP
'''
with localcontext() as ctx:
    ctx.rounding = ROUND_HALF_UP
    for i in range(1,15,2):
        upFloat = Decimal(i) / 2
        upRound = upFloat.to_integral_value()
        print(str(upFloat) + " -> " + str(upRound))
    print( '0.4 -> ' + str( Decimal(0.4).to_integral_value() ) )
