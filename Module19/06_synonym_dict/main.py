kolvo = int(input('Введите количество пар слов: '))
word_dict = {}

for i in range(1,kolvo +1):
    print(f'{i}-я пара:',end=' ')
    word = input().lower().split(' — ')
    print(word)
    word_dict.update({word[0]:word[1]})

while True:
    word = input('Введите слово: ').lower()
    if word == 'end':
        break
    elif word in word_dict:
        print('Синоним: ',word_dict[word])
    else:
        print('Такого слова в словаре нет.')
