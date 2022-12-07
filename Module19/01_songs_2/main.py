violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

kolvo_music = int(input('Сколько песен выбрать? '))
time_play = 0
for i in range(1,kolvo_music+1):
    print(f'Название {i}-й песни:',end= ' ')
    name_musik = input()
    if name_musik in violator_songs:
        time_play += violator_songs[name_musik]
    else:
        print('Ошибка трек не найден!\nДобавьте новый трек в словарь!')
print(f'\nОбщее время звучания песен: {round(time_play,2)} минуты')