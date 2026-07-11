def add(a, b):
    return a + b
def subtract(a , b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
try:
    print("calculator")
    print("1 . add")
    print("2 . subtract")
    print("3 . multiply")
    print("4 . divide")
except ZeroDivisionError:
    print("cannot divide by zero")
num1 = float(input("enter your first number here"))
num2 = float(input("enter yor second number here"))
choice = input("enter 1 for add, 2 for substract, 3 for multiply, 4 for divide")
if choice == 1:
    print(add(num1,num2))
elif choice == 2:
    print(subtract(num1,num2))
elif choice == 3:
    print(multiply(num1,num2))
elif choice == 4:
    print(divide(num1,num2))
else:
    print("invalid choice")