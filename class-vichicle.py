class Car:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
car1= Car("toyata",150)
car2= Car("subaru",400)
print(car1.mileage, car1.max_speed)
print(car2.mileage, car2.max_speed)