import random

kolvo_chisel = int(input('Количество чисел в списке: '))

nachalnyi_spisok = [random.randrange(0,3) for _ in range(kolvo_chisel)]
last_spisok = [x for x in nachalnyi_spisok if x != 0]

print('Список до сжатия: ',nachalnyi_spisok)
print('Список после сжатия: ',last_spisok)
