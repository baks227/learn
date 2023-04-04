stroka = 'abcd'
kort = (10, 20, 30, 40)
kort_new, j = [], 0

print('Результат:')
for i in stroka:
    kort_new = [i,kort[j]]
    j += 1
    print(kort_new)