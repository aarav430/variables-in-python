def factoral(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factoral(x-1)
print(factoral(5))

    