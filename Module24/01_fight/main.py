import random

class Warrior:
    def __init__(self,index):
        self.role = 'warrior'
        self.HP = 100
        self.damage = 20
        self.index = index
    def fight (self,Warrior_1,Warrior_2):
        while True:
            self.index = random.randint(1, 2)
            if self.index == 1:
                print(f'Воин_{Warrior_1.index} атакует Война_{Warrior_2.index}')
                Warrior_2.HP -= Warrior_1.damage
                if Warrior_2.HP == 0:
                    print(f'Воин_{Warrior_1.index} победил Война_{Warrior_2.index}')
                    break
                print(f'{Warrior_2.HP}HP- Оставшиеся здоровье Война_{Warrior_2.index}')
            elif self.index == 2:
                print(f'Воин_{Warrior_2.index} атакует Война_{Warrior_1.index}')
                Warrior_1.HP -= Warrior_2.damage
                if Warrior_1.HP == 0:
                    print(f'Воин_{Warrior_2.index} победил Война_{Warrior_1.index}')
                    break
                print(f'{Warrior_1.HP}HP- Оставшиеся здоровье Война_{Warrior_1.index}')



Warrior_1 = warrior(1)
Warrior_2 = warrior(2)
winner = warrior.fight(warrior,Warrior_1,Warrior_2)