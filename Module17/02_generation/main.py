N = int(input('Введите длину списка: '))

gen_list = [(x**0 if x % 2 == 0 else x % 5) for x in range(N)]

print('Результат: ', gen_list)