m1=int(input("enter mark 1: "))
m2=int(input("enter mark 2: "))
m3=int(input("enter mark 3: "))
m4=int(input("enter mark 4: "))
m5=int(input("enter mark 5: "))
avg=(m1+m2+m3+m4+m5)/5
print("average is ",avg)
if avg >= 91:
    print("a1")
elif avg >=81 :
    print("a2")
elif avg >=71 :
    print("b2")
elif avg >=61 :
    print("c2")
else :
    print("fail")