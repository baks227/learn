nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def rec(*list):
    rec_fun = []
    for elem in list:
        try:
            rec_fun +=rec(*elem)
        except TypeError:
            rec_fun.append(elem)
    return rec_fun

print('Ответ:', rec(nice_list))
