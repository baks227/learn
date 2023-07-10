line_count = 0

try:
    with open('people.txt','r',encoding='UTF-8') as people_file:
        sym_sum = 0
        for i_line in people_file:
            try:
                line_count += 1
                length = len(i_line)
                if i_line.endswith('\n'):
                    length -= 1
                sym_sum += length
                if length < 3:
                    raise BaseException
            except BaseException:
                print('\nОшибка: Длина {} строки меньше 3х символов!'.format(line_count))
except FileNotFoundError:
    print('Файл не найден!')

finally:
    print('Найденная сумма символов: ',sym_sum)