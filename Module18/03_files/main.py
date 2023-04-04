name_file = input('Введите название файла: ')

symbol = '@№$%^&\*()'
for i in symbol:
    if name_file.startswith(i):
        print('\nОшибка: название начинается на один из специальных символов.')
        break
    if not (name_file.endswith('.txt') or name_file.endswith('.docx')):
        print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx.')
        break
    else:
        print('\nФайл назван верно.')
        break




