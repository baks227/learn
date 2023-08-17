class Element:
    def __init__(self, name):
        if name in ('Вода', 'Воздух', 'Огонь', 'Земля'):
            self.name = name
        elif name in ('Шторм', 'Пар', 'Грязь', 'Молния', 'Пыль', 'Лава'):
            self.name = name
        else:
            raise ValueError('Такого элемента нет!')

    def __add__(self, other):
        if {self.name, other.name} == {'Вода', 'Воздух'}:
            return Element('Шторм')
        elif {self.name, other.name} == {'Вода', 'Огонь'}:
            return Element('Пар')
        elif {self.name, other.name} == {'Вода', 'Земля'}:
            return Element('Грязь')
        elif {self.name, other.name} == {'Воздух', 'Огонь'}:
            return Element('Молния')
        elif {self.name, other.name} == {'Воздух', 'Земля'}:
            return Element('Пыль')
        elif {self.name, other.name} == {'Огонь', 'Земля'}:
            return Element('Лава')
        elif self.name == other.name:
            print('Создание нового элемента не имеет смысла, элементы равны!\n')
            return Element(self.name)
        else:
            raise AttributeError('Такое сочетание не предусмотрено!')

elem_1 = Element('Вода')
elem_2 = Element('Воздух')
elem_3 = elem_1 + elem_2
print(elem_1.name, '+', elem_2.name, '=', elem_3.name)
