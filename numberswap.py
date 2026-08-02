
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

temp = a
a = c
c = b
b = temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
print("c =", c)