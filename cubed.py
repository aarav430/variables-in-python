def cube(number):
    return number * number * number
def check(number):
    if number %3 == 0:
        result= cube(number)
        print(result)
    else:
        print("number is not divisable by 3")
check(21)