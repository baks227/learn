# ЗАдача 7
def search_year():
  j,k,a = 0,0,''

  y1 = int(input('Введите первый год: '))
  y2 = int(input('Введите второй год: '))
  print('\nГоды от',y1,'до',y2,'с тремя одинаковыми цифрами:')
  while y1 != y2:
    for i in str(y1):
        a = i
        for k in str(y1):
          if a == k:
            j += 1
        if j == 3:
          print(y1)
          break
        j = 0
    y1 += 1
search_year()
