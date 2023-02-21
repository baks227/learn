def search_family():
    familya = input('Введите фамилию: ').lower()
    for i_person in num_dict:
        if familya in i_person[1].lower() or familya + 'а' in i_person[1].lower() \
                or familya[:len(familya) - 1] in i_person[1].lower():
            print(i_person[0], i_person[1], num_dict[i_person])
def add_contact():
    name = input('Введите имя и фамилию нового контакта (через пробел): ')
    name = tuple(name.split())
    if name not in num_dict:
        num = int(input('Введите номер телефона: '))
        num_dict[name] = num
    else:
        print('Такой человек уже есть в контактах.')
    print('Текущий словарь контактов:',num_dict)
    return num_dict

num_dict = {}
while True:
    act = int(input('Введите номер действия: \n1. Добавить контакт \n2. Найти человека \n'))
    if act == 1:
        add_contact()
    elif act == 2:
        search_family()
    else:
        print('Ошибка!!!')
        break