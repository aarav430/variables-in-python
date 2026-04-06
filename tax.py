units=int(input("how many units do you have"))
if units < 50 :
    cost=2.60
    tax=25
elif units < 100 :
    cost=3.25
    tax=35
elif units < 200 :
    cost=5.25
    tax=45
else:
    cost=8.45
    tax=75 
bill=units*cost+tax
print("total electrity bill" , bill)