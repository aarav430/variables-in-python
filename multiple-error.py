try:
    num1 = int(input("enter number 1 here"))
    num2 = int(input("enter second number here"))
    result = num1 / num2
    print(result)
except ValueError:
    print("put only numbers")
except ZeroDivisionError:
    print("do not divide by zero")
finally:
    print("program has done running")
    