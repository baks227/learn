def shifr_cesarya(message,sdvig):
    alfabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л',
    'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х'
    , 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    shifr_message = [(x if alfabet.count(x) == 0 else (alfabet[alfabet.index(x)+sdvig] if alfabet.index(x)+sdvig < 32
                     else alfabet[(alfabet.index(x) + sdvig) % (len(alfabet))]))
                     for x in message]
    return shifr_message

shifr_message = shifr_cesarya(input('Введите сообщение: '),int(input('Введите сдвиг: ')))
print('Зашифрованное сообщение: ',end ='')
for i in shifr_message:
    print(i,end ='')