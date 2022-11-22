message = str(input('Введите строку: '))
cnt,message_upd = 1,''

for i in range(len(message)):
    if i == (len(message)-1):
        message_upd += message[i]+str(cnt)
    else:
        if message[i] == message[i+1]:
            cnt += 1
        else:
            message_upd += message[i]+str(cnt)
            cnt = 1

print('Закодированная строка: ',message_upd)