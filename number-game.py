import random
computer=random.randint(1,10)
user=int(input("guess a number between 1 and 10"))
if user == computer:
    print("congratualtions you guessed the right number")
else:
    print("sorry wrong guess")