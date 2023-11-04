class Weapon(object):
    all_model = []

    def __init__(self, model, caliber, year):
        self.model = model
        self.caliber = caliber
        self.year = year
        self.all_model.append(model)

    @staticmethod
    def shooting():
        print('Shot, shot, shot')

    @classmethod
    def count_models(cls):
        return len(cls.all_model)

    @property
    def full_information(self):
        return f'{self.model}, {self.year}, {self.caliber}'

    @full_information.setter
    def full_information(self, new):
        index = Weapon.all_model.index(self.model)
        self.model, self.year, self.caliber = new.split(', ')
        Weapon.all_model[index] = self.model


if __name__ == '__main__':
    a = Weapon('AK-74', 5.45, 1974)
    b = Weapon('AR-15', 5.56, 1959)

    a.shooting()
    b.shooting()
    Weapon.shooting()

    print('-' * 50)

    print(a.count_models())
    print(b.count_models())
    print(Weapon.count_models())

    print('-' * 50)

    print(a.full_information)
    print(a.model)
    print(a.year)
    print(a.caliber)

    print('-' * 50)

    a.full_information = 'RPG-7, 1964, 40'
    print(a.full_information)
    print(a.model)
    print(a.year)
    print(a.caliber)

    print('-' * 50)

    print(Weapon.all_model)
