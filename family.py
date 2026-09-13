class familymember:
    def __init__(self, eye_colour, height_cm):
        self.eye_colour = eye_colour
        self.height_cm = height_cm
    def show_traits(self):
        print("eye_colour:" , self.eye_colour)
        print("height_cm:" , self.height_cm)
class kid(familymember):
    def __init__ (self, name ,age, eye_colour, height_cm):
        self.name = name
        self.age = age
        super().__init__ (eye_colour, height_cm)
    def show_traits(self):
        print("name" , self.name)
        print("age" , self.age)
        super().show_traits()
    def favorite_hobby(self , hobby):
        print(self.name, 'loves', hobby)
child =kid("maya", 10, "brown", 140)
child.show_traits()
child.favorite_hobby("painting")
print("is kid a subclass of familymember?" , issubclass(kid, familymember))