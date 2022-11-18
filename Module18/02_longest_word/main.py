stroka = input('Введите строку: ')

longer_str = max(stroka.split(),key=len)

print(f'Самое длинное слово: {longer_str}\nДлина этого слова: {len(longer_str)}')