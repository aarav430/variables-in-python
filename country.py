country = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
code = input("enter country name")
if code in country:
    print("county code ", country[code])
else:
    print("country not found")