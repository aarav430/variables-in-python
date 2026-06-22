for num in range (1, 31):
    if num %20==0:
        print("twisted")
    elif num %15==0:
        pass
    elif num %5==0:
        print("fizz")
    elif num %3==0:
        print("buzz")
    else:
        print(num)