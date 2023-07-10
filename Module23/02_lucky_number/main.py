import random

numbers_sum = 0
flag = True
open('out_file.txt', 'w', encoding='utf-8')# для очистки файла

while flag:
    try:
        random_number = random.randint(1, 13)
        number = int(input("Введите число: "))
        if random_number == 3:
            print(random_number)
            # 3 - случайное исключение в диапазоне (1 к 13)
            raise ValueError
        numbers_sum += number
        if numbers_sum >= 777:
            print("Вы успешно выполнили условие для выхода из порочного цикла!")
            flag = False
    except ValueError:
        print("Вас постигла неудача!")
        flag = False
    else:
        with open("out_file.txt", "a", encoding="utf-8") as out_file:
            out_file.write(f"{number}\n")
out_file.close()