palki = ['I' for _ in range(int(input('Количество палок: ')))]

for i in range(1,int(input('Количество бросков: ')) +1):
    print('Бросок',i,end='')
    for j in range(int(input('. Сбиты палки с номера '))-1,int(input('по номер: '))):
        palki[j] = '.'

print('Результат:',end='')
for i in palki:
    print(i,end='')