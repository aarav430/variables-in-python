import random
choices=["rock","paper","scissors"]
computer=random.choice(choices)
user=input("enter rock, paper or scissors")
print("computer chose",computer)
print("user chose",user)
if user == computer:
    print("it is a tie")
elif(user == "rock" and computer == "scissors") or \
    (user == "rock" and computer == "paper") or \
    (user == "scissors" and computer == "paper"):
    print("you win")
elif user in choices:
    print ("computer wins")
else:
    print("invalid choice")