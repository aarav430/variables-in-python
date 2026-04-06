print("select your ride")
print("1.bike")
print("2.car")

choice=int(input("enter your choice: "))
if choice==1:
    print("select your bike type")
    print("1.sports bike")
    print("2.scooter")
    bike=int(input("enter your choice :"))
    
    if bike== 1:
        print("you have selected the sports bike")
    else:
        print("you have selected a scooter")
elif choice==2 :
    print("select your car type")
    print("1.sudan")
    print("2.suv")
    car=int(input("input you choice :"))
    if car == 1:
        print("you have selected sudan")
    else:
        print("you have selected the suv")
else:
    print("invalid choice")
