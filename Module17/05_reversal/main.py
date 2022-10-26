word = input('Введите строку: ')

fragment = word[word.find('h')+1:word.rfind('h')]

print(fragment[::-1])