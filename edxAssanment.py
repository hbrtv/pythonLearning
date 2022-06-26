annualInterestRate = 0.043
balance = 10000.00

lowerBalance = balance / 12
monthInterestRate = annualInterestRate / 12
upperBalance = balance *( ( 1 + monthInterestRate) ** 12) /12
while((upperBalance - lowerBalance) >= 0.00999):
    tmp = (upperBalance + lowerBalance) / 2
    if(tmp * (( 1 + monthInterestRate) ** 12 - 1) / monthInterestRate  > balance *( ( 1 + monthInterestRate) ** 12)):
        upperBalance = tmp
    else:
        lowerBalance = tmp
    
    print("tmp:{0:8f}".format(tmp))
    gap = tmp * (( 1 + monthInterestRate) ** 12 - 1) / monthInterestRate   -  balance *( ( 1 + monthInterestRate) ** 12)
    print("the gap is : {0:8.3f}".format(gap) )
    prise = upperBalance - lowerBalance
    print("the prise is : {0:8f}".format(prise))

