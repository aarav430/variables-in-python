def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

choice=input("enter a operation (+ , - , * , / ): ")
num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
if choice=="+":
    print("answer=", add(num1,num2))
elif choice=="-":
    print("answer=", subtract(num1,num2))
elif choice=="*":
    print("answer=", multiply(num1,num2))
elif choice=="/":
    print("answer=", divide(num1,num2))
else:
    print("invalid choice")