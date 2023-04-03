def competition_protocol():
    records = list()
    records_num = int(input('Сколько записай вносится в протокол? '))
    print('Записи (Результат и имя) - введите через пробел')
    for attempt in range(records_num):
        score, name = input(f'{attempt + 1}-я запись: ', ).split()
        records.append((score,records_num - attempt, name))
    result(sorted(records))

def result(protocol):
    players, top, place = {}, set(), 1
    print('\nИтоги соревнований: ')
    for id_rec, record in enumerate(protocol[::-1]):
        score, _, name = record
        if name not in players or int(score) > int(players[name]):
            players[name] = score
    for name, score in players.items():
        if name not in top and place <= 3:
            top.add(name)
            print(f"{place}-е место: {name} ({score})")
            place += 1
        elif place >3:
            break

competition_protocol()