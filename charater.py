word = input("enter a word here:")

ch = input("enter a charater to find:")

count = 0
for letter in word:
    if letter == ch:
        count += 1
print(count)