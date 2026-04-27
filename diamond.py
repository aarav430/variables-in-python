rowSize = int(input("Enter the number of rows: "))

if rowSize % 2 == 0:
    halfDiamRow = int(rowSize / 2)
else:
    halfDiamRow = int(rowSize / 2) + 1

space = halfDiamRow - 1

# Upper part
for i in range(1, halfDiamRow + 1):  # rows
    for j in range(1, space + 1):    # spaces
        print(end=" ")
    space = space - 1

    num = 1
    for j in range(2 * i - 1):       # numbers
        print(num, end="")
        num = num + 1

    print()

space = 1

# Lower part
for i in range(1, halfDiamRow):      # rows
    for j in range(1, space + 1):    # spaces
        print(end=" ")
    space = space + 1

    num = 1
    for j in range(1, 2 * (halfDiamRow - i)):  # numbers
        print(num, end="")
        num = num + 1

    print()