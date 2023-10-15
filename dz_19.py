class Auto(object):
    brand = ''
    age = 0
    color = ''
    mark = ''
    weight = 0

    def __init__(self, brand, age, mark, color='Not entered', weight='Not entered'):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"""Brand: {self.brand}
Age: {self.age}
Mark: {self.mark}
Color: {self.color}
Weight: {self.weight}"""

    def move(self):
        print('Move')

    def stop(self):
        print('Stop')

    def birthday(self):
        self.age += 1
        print(f'Your car is a year older. It is {self.age}')


bmw = Auto('BMW', 8, 'M5')
print(bmw)
bmw.move()
bmw.stop()
bmw.birthday()
bmw.birthday()
