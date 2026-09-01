class Parrot:
    type = "bird"
    def __init__(self, age, name):
        self.name = name
        self.age = age
blu = Parrot("blu",14)
woo = Parrot("woo",16)
print("blu is a {}".format(blu.type))
print("woo is a {}".format(woo.type))
print("blu is {} years old".format(blu.name,blu.age))
print("woo is {} years old".format(blu.age,blu.name))