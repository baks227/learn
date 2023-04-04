kolvo_order = int(input('Введите количество заказов: '))
order_dict = {}

for i in range(1,kolvo_order+1):
    print(f'{i}-й заказ: ',end='')
    order = input()
    fio,pizza,amount = order.rsplit(maxsplit=3)
    amount = int(amount)
    if fio not in order_dict:
        order_dict[fio] = {pizza:amount}
    else:
        if pizza not in order_dict[fio]:
            order_dict[fio][pizza] = amount
        else:
            order_dict[fio][pizza] += amount
print()

for fio, order in sorted(order_dict.items()):
    print(f'{fio}:')
    for pizza, amount in sorted(order.items()):
        print('\t', pizza,':', amount)