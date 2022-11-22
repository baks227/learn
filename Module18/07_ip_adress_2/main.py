ip = input('Введите IP-адрес: ')

ip_mass = ip.split('.')

if len(ip_mass) != 4:
    print('Адрес — это четыре числа, разделённые точками.')
else:
    num,out = 0,0
    for i in ip_mass:
        if i.isdigit():
            num += 1
            if int(i)>255:
                out += 1
                print(f'{i} превышает 255')
        else:
            print(f'{i} - это не целое число.')
    if num == 4 and out == 0:
        print('IP-адрес корректен.')