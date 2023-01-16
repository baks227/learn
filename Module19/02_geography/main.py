kolvo_country = int(input('Количество стран: '))
s_dict = {}
for i in range(kolvo_country):
    value = input('{}-я страна: '.format(i + 1)).split()
    for city in value[1:]:
        s_dict[city] = value[0]
for i in range(3):
    city = input('\n{}-й город: '.format(i + 1))
    country = s_dict.get(city)
    if country:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f' По городу {city} данных нет.')
