str_1 = input('Первая строка: ')
str_2 = input('Вторая строка: ')

if str_1 == str_2:
    print('\nСтроки одинаковые.')
else:
    if len(str_1) != len(str_2):
        print('\nСтроки имеют разную длину.')
    else:
        shift = 1
        flag = True
        for i in range(len(str_1) - 1):
            str_2 = str_2[-1] + str_2[:-1]
            if str_1 == str_2:
                print(f'\nПервая строка получается из второй со сдвигом {shift}.')
                flag = False
                break
            else:
                shift += 1
        if  flag:
            print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
