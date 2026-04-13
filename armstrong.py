num=int(input("enter number here"))
temp=num
sum=0
while temp>0:
    digits=temp % 10
    sum+=digits**3
    temp//=10
if sum==num:
    print(num, "it is an armstrong number")
else :
    print(num, "is not an armstrong number")
