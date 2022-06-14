# ЗАДАЧА 3
def sum_n() -> object:
  S = int(sum(map(int,str(N))))
  return S
def col_chair():
    M = str(N)
    Col= 0
    for i in M:
        Col += 1
    b = int(Col)
    return b


N = int(input('Введите число: '))
print('\nCумма чисел:', sum_n())
print('Количество цифр в числе:',col_chair())
print('Разность суммы и количества цифр: ',sum_n()-col_chair())
