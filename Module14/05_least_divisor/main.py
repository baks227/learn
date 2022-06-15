# задача 5
def ND():
  n = int(input('Введите число: '))
  d = n
  for i in range(n+1):
      n2 = i
      if n > n2 > 1 and n % n2 == 0 and n2 < d:
        d = n2
  print('Наименьший делитель, отличный от единицы: ',d)
ND()