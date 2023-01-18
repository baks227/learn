max_num = int(input('Введите максимальное число: '))
all_nums = {x for x in range(max_num+1)}
while True:
    guess = input('\nНужное число есть среди вот этих чисел: ')
    if guess == 'Помогите!':
        break
    guess = {int(x) for x in guess.split()}
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        all_nums &= guess

    else:
        all_nums -= guess
print('Артём мог загадать следующие числа:',*all_nums)


