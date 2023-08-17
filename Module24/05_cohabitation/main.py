import random


class Human:
    def __init__(self, name, satiety=50):
        self.name = name
        self.satiety = satiety

    def day(self, action):
        if self.satiety < 20 and Home.fridge >= 10:
            self.satiety += 10
            Home.fridge -= 10
            print(f'{self.name} - покушал')
        elif Home.fridge < 10 and Home.cash > 0:
            Home.fridge += 30
            Home.cash -= 10
            print(f'{self.name} - сходил в магазин')
        elif action == 1:
            Home.cash += 50
            self.satiety -= 10
            print(f'{self.name} - работает')
        elif action == 2:
            self.satiety += 10
            Home.fridge -= 10
            print(f'{self.name} - пошел кушать')
        else:
            self.satiety -= 10
            print(f'{self.name} - играем')


class Home:
    cash = 0
    fridge = 50

    def __init__(self, man_1, man_2):
        self.human_1 = man_1
        self.human_2 = man_2

    def __add__(self,human_1,human_2):
        self.cash = human_1.money + human_2.money
        self.fridge = human_1.food + human_2.food

    def is_life(self):
        if self.human_1.satiety == 0 or self.human_2.satiety == 0:
            return True, print('Эксперимент не удался!\nОдин из участников умер.')


h1 = Human('Andrey')
h2 = Human('Elena')

home_life = Home(h1,h2)

for day in range(1, 366):
    print(f'\nДень {day}')
    if day == 365:
        print('Эксперимент удался, Все выжили!')
        break
    elif home_life.is_life():
        break
    else:
        d_6 = random.randint(1, 6)
        h1.day(d_6)
        h2.day(d_6)
