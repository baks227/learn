guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

party_time = ''
while party_time != 'Пора спать':
    print('Сейчас на вечеринке',len(guests),'человек:', guests)
    party_time = input('Гость пришёл или ушёл? ')

    if party_time == 'пришел':
        name_party = input('Имя гостя: ')
        if  len(guests)+1 <= 6:
            guests.append(name_party)
            print('Привет,',name_party)
        else:
            print('Прости,',name_party,',но мест нет.')
        print()
    elif party_time == 'ушел':
        name_party = input('Имя гостя: ')
        guests.remove(name_party)
        print('Пока,',name_party,'!\n')
    elif party_time == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')

