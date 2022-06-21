# ЗАдача 6
def search(x,y,r):
  if -r <= x <= r and -r <= y <= r:
    print('Монетка где-то рядом')
  else:
    print('Монетки в области нет')
print('Введите координаты монетки: ')
x = float(input('\nX: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
search(x,y,r)