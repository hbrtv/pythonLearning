text = "apple today is ${price:>18,.4f}"
print(text.format(price = 9999.99))

tab = {"server":"127.0.0.1","port":1080,"fast-open":True}

print("ss server address is : {0[server]:20s} , ss port is {0[port]:>8d} , and fast-open option is : {0[fast-open]}".format(tab))


pi = 3.1415926
e = 2.718281828904590

print("pi with two decimal pricise is: {pi:>5.2f}, and nature number with four decimal precise is : {e:<5.4f}".format(pi = 3.1415925,e = 2.718281828459045))
print("pi with two decimal pricise is: {0:>5.2f}, and nature number with four decimal precise is : {1:<5.4f}".format(pi,e))
