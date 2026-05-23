import random
secrecttnumber = random.randint(1,50)
attempt=5
count=0
print("welcome to the guessing game you have 5 attempts to guess a number between 1 to 50")
while count < attempt:
    number=int(input("enter number"))
    count += 1 
    if number == secrecttnumber:
        print("you win")
        break
    else:
        difference= abs(secrecttnumber-number)
        if difference > 20:
            print("you are ice cold")
        elif difference > 10:
            print("you are cold")
        elif difference > 5:
            print("you are warm")
        else:
            print("you are hot")
            