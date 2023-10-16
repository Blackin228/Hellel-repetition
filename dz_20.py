from dz_19 import Auto
from time import sleep


class Truck(Auto):
    max_load = 0

    def __init__(self, max_load, brand, age, mark, color='Not entered', weight='Not entered'):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def __str__(self):
        return f"""Brand: {self.brand}
Age: {self.age}
Mark: {self.mark}
Color: {self.color}
Weight: {self.weight}
Max load: {self.max_load}"""

    def move(self):
        print('Attention')
        super().move()

    def load(self):
        sleep(1)
        print('Load')
        sleep(1)


class Car(Auto):
    max_speed = 0

    def __init__(self, max_speed, brand, age, mark, color='Not entered', weight='Not entered'):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def __str__(self):
        return f"""Brand: {self.brand}
Age: {self.age}
Mark: {self.mark}
Color: {self.color}
Weight: {self.weight}
Max speed: {self.max_speed}"""

    def move(self):
        super().move()
        print(f'Max speed is {self.max_speed}')


truck_1 = Truck(15000, 'Volvo', 15, 'm15')
truck_2 = Truck(30000, 'DAF', 6, 'xf')
print(truck_1)
print(truck_2)
print(truck_1.move())
print(truck_2.move())
print(truck_1.load())
print(truck_2.load())

car_1 = Car(260, 'BMW', 5, 'M5')
car_2 = Car(300, 'Porsche', 4, 'Cayenne')
print(car_1)
print(car_2)
print(car_1.move())
print(car_2.move())
