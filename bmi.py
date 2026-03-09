weight=float(input("enter your weight here"))
height=float(input("enter your height here"))
BMI=weight/(height**2)
print("your BMI is ",BMI)
if BMI< 18.5:
    print("you are underweight")
elif BMI < 25:
    print("your weight is normal")
else :
    print("you are ober weight")
