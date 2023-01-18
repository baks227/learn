text_write = input('Введите текст: ')
invers_dict,origin_dict = {},{}
print('Оригинальный словарь частот:')

for sym in text_write:
    if sym in origin_dict:
        origin_dict[sym] += 1
    else:
        origin_dict[sym] = 1

for key,values in sorted(origin_dict.items()):
    print(key,':',values)
keys = []

for v in range(1,max(origin_dict.values()) +1):
    for key,values in origin_dict.items():
        if values == v:
            keys += key
    invers_dict.update({v : keys})
    keys = []
print('\nИнвертированный словарь частот:')

for key,values in invers_dict.items():
    print(key,':',values)