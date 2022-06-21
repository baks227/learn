# Задача 4

def reverse_n(n,word):
  m = ".".join(map("".join, map(reversed, n.split("."))))

  print(word+'наоборот: ',m)#если нули не нужны, меняем m на int(m)
  return m
n1 = input('Введите первое число: ')
n2 = input('Введите второе число: ')
sum = float(reverse_n(n1,'\nПервое число '))
sum += float(reverse_n(n2,'Второе число '))
print('Cумма: ',sum)



