valid = False
while not valid:
    num = int(input("enter number here"))
    if num %2 == 0 :
        valid = True
        print("number is divisable by two")
        while True:
            text = input("type 'stop' to end or press enter to print bye :")
            if text.lower()=="stop":
                break
            print("bye")
        else:
            print("enter a evem number")