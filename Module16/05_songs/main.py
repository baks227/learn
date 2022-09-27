violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
much_songs = int(input('Сколько песен выбрать? '))
time_songs = 0
for i in range(much_songs):  # цикл перехода по внутренним спискам
    print('Название',i + 1,end = '')
    name_songs = input('-й песни: ')
    for index in range(len(violator_songs)):
        if violator_songs[index][0] == name_songs: # поиск совпадений в имеющемся списке позиций заданных пользователем
            time_songs += violator_songs[index][1]
print('\nОбщее время звучания песен:',round(time_songs,2),'минуты') # вывод количества совпадений
