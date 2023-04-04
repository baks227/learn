def input_list():
    man = int(input('Кол-во человек: '))
    debt = int(input('Долговых расписок: '))

    lists = []
    for i in range(1,man +1):
        lists.append([i,0])
    return lists,debt

def oper_list(debt):
    for i in range(1,debt+1):
        print('\n',i,'-я расписка')
        whom = int(input('Кому: '))
        from_wh = int(input('От кого: '))
        how_many = int(input('Сколько: '))
        for j in range(1,len(new_list) + 1):
            if whom == j and from_wh != whom:
                new_list[whom-1][1] -= how_many
                new_list[from_wh - 1][1] += how_many
    print('\nБаланс друзей:')
    for i in range(len(new_list)):
        print( new_list[i][0],':',new_list[i][1])

new_list,debt = input_list()
oper_list(debt)
