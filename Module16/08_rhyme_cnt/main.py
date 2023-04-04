def input_list():
    man = int(input('Кол-во человек: '))
    how = int(input('Какое число в считалке? '))
    print('Значит, выбывает каждый ',how,'-й человек')
    lists = []
    for i in range(1,man +1):
        lists.append(i)
    return lists,how

def oper_list(hows):
    i = 0
    while len(new_list) != 1:
        res = abs(len(new_list)-hows)
        while res > len(new_list):
            res -= len(new_list)
            if res == 1:
                i = 0
        print('\nТекущий круг людей:',new_list)
        print('Начало счёта с номера',new_list[i])
        print('Выбывает человек под номером',new_list[i+res-1])
        new_list.pop(i+res-1)
        i = len(new_list) - res - 1
    print('\nОстался игрок под номером :', new_list[0])


new_list,hows = input_list()
oper_list(hows)
