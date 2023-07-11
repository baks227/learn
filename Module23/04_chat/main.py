name = input('Введите ваше имя:\n')
flag = True
print('Здравствуй,',name) # для того, чтобы сменить пользователя нужно перезапустить программу
while flag:
    with open('name_list.txt', 'r+', encoding='utf-8') as name_list, \
            open('chat_log.txt', 'a+', encoding='utf-8') as chat:
        if name not in name_list.read():
            name_list.write(f'\n{name}') #записываем имена, надеемся на уникальные.
        print('1) Посмотреть текущий текст чата.\n'
              '2) Отправить сообщение (затем вводит сообщение).\n'
              '0) Завершение программы!')
        try:
            key = int(input())
            if key == 1:
                chat = open('chat_log.txt','r+',encoding='utf-8')
                print('Сообщения в чате:\n',chat.read()) #читаем чат
            if key == 2:
                message = input('Введите сообщение:\n')
                chat.write(f'\n{name}:    {message}') #пишем в чат
                chat.close()
            if key == 0:
                print('Заканчиваю работать!')
                flag = False
        except ValueError:
            print('Опечатка вводе данных!\nПовторите ввод!!!\n')


