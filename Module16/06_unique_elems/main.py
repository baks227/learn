def gen_list (n,num):
    generation = []
    for i in range(n):
        print('Введите',i+1,'число для',num,'списка: ',end='')
        count = int(input())
        generation.append(count)
    return generation
def gen_new_lists():
    i = 0
    sum_list = first_list + second_list
    while i != len(sum_list):
        for x in sum_list:
            if sum_list.count(x) != 1:
                sum_list.remove(x)
        i += 1
    return sum_list
first_list = gen_list(3,'первого')
second_list = gen_list(7,'второго')
uni_list = gen_new_lists()
print('\nПервый список:',first_list)
print('Второй список',second_list)
print('\nНовый первый список с уникальными элементами:',uni_list)
