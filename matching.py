word = ["abc","xyz","aba","1221","aa","x"]
count = 0
for i in word:
    if len(i)>=2 and i[0]==i[-1]:
        count += 1
print(count)