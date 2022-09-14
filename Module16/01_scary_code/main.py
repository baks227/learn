def input_list(): #Функция ввода переменных
    a = [1, 5, 3]
    b = [1, 5, 1, 5]
    c = [1, 3, 1, 5, 3, 3]
    return a,b,c
    pass

def first_oper_list(a): #Функции поиска цифры 5 при первом обьединении
    t = 0
    for i in b:
        a.append(i)
    for i in a:
        if i == 5:
            t += 1
    return t
    pass

def second_oper_list(a,c): #Функция поиска цифры 3 при втором обьединении
    d = []
    for i in a:
        if i != 5:
            d.append(i)
    for i in c:
        d.append(i)
    t = 0
    for i in d:
        if i == 3:
            t += 1
    return t,d
    pass

def output(t1,t2,d): # Функция вывода результатов
    print('Результат работы программы:')
    print('Кол-во цифр 5 при первом объединении:',t1)
    print('Кол-во цифр 3 при втором объединении:',t2)
    print('Итоговый список:',d)

a,b,c = input_list() # Получаем списки
t1 = first_oper_list(a) # Ищем 5 после объединения
t2,d = second_oper_list(a,c) #Ищем 3 после объединения
output(t1,t2,d) # Выводим результат
