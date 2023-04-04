def gen_list(something,someth):
    print('\nКол-во',something,': ', end = '')
    quantity = int(input())
    generation = []
    for i in range(quantity):
        print('Размер', i + 1,someth,': ',end='')
        count = int(input())
        generation.append(count)
    return generation
def gen_new_lists():
    i = 0
    for x in first_list:
        for y in second_list:
            if x == y:
                second_list.remove(y)
                i += 1
                break
    return i
first_list = gen_list('коньков','пары')
second_list = gen_list('людей','человека')

print('\nНаибольшее кол-во людей, которые могут взять ролики:',gen_new_lists())