odd = 9
dup = 8

# divided 
half = odd/2.0
roundedHalf = odd//2

remainder = odd%2

print("half with pricise is:  %5d" %half)

print("rounded half is: %5i" %roundedHalf)

print("remainder is : %5i" %remainder)


text = "apple today is ${price:.4f}"
print(text.format(price = 999.99))
