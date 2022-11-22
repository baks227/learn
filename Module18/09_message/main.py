message = input('Сообщение:').split()

new_message = []

for word in message:
    if word.isalpha():
        new_message += ''.join(reversed(word))
    else:
        i = 0
        for char in word:
            if char.isalpha():
                i += 1

            else:
                new_message += ''.join(reversed(word[0:i]))
                new_message += ''.join(char)
            if not char.isalpha():
                new_message += ''.join(reversed(word[i+1:len(word)]))
                break
    new_message += ''.join(' ')
print(''.join(new_message))