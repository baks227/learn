def input_list(): #составляем ширенгу по заданным параметрам
    height_min = int(input('Введите наименьший рост: '))
    height_max = int(input('Введите наибольний рост: '))
    step = int(input('Введите шаг: '))
    rank = []
    for i in range(height_min,height_max+1,step):
        rank.append(i)
    return rank
def operation_list(rank_1,rank_2): #складываем списки и сортируем суммарную шеренгу
    rank = rank_1+rank_2
    print(rank)
    rank.sort()
    return rank
def output_result(sort_rank): #выводим результат
    print('Отсортированный список учеников:',sort_rank)

rank_1= input_list()#составляем ширенгу по заданным параметрам
rank_2 = input_list()#составляем ширенгу по заданным параметрам
sort_rank = operation_list(rank_1,rank_2)#складываем ширенги и сортируем общую
output_result(sort_rank) #Выводим результат