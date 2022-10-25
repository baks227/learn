text = input('Введите текст: ')

vowel = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
vowel_str = [x for x in text for y in vowel if x == y]

print('\nСписок гласных букв: ',vowel_str,'\nДлина списка: ',len(vowel_str))