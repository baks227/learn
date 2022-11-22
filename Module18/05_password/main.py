password = input('Придумайте пароль: ')

while True:
    if not password.isalnum() or sum(map(str.isupper,password)) <= 1 or len(password) < 7:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
    password = input('Придумайте пароль: ')


