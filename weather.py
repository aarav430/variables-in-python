day=(1, 0, 0, 0, 1, 1, 0)
rainy = day.count(1)
sunny = day.count(0)
print(rainy , ":rainy")
print(sunny , ":sunny day")
if rainy > sunny:
    print("it will be rainy")
else:
    print("it will be sunny")