num = int(input('Введите num: '))

def num_scale(num):
    if num >= 1:
        num_scale(num - 1)
        print(num)


num_scale(num)
