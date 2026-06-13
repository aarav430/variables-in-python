def  total_calc(bil_amount, tip_per):
    tip=tip_per * bil_amount / 100 
    total= bil_amount + tip 
    print(total)
total_calc(2000, 10)