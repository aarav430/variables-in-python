number=input("enter a number here")
middle=number[1:-1]
product=1
for digit in middle:
    product=product* int(digit)
print(product)