medical=input("do you have a medical condition(y/n)")
if medical=="y" :
    print("you can take the exam")
else : 
    attendance=int(input("enter you attendace percentage"))
    if attendance >= 75 :
        print("you are allowed to take the exam")
    else : 
        print("you are not allowed to take the exam")