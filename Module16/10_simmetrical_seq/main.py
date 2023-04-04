num = int(input('Кол-во чисел: '))
arr = []

for i in range(num):
    arr.append(int(input('Число: ')))
print('\nПоследовательность:',arr)
counter = 0
while arr != arr[::-1]:
    arr.insert(num, arr[counter])
    counter += 1

print('Нужно приписать чисел:', counter)
print('Сами числа:', arr[:counter][::-1])