students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def first_zadanie(dict):
    id_ages = []
    intersting = []
    len_fam = 0
    for id, ages in dict.items():
        for a in ages.items():
            if 'age' in a:
                age = a[1]
                id_ages.append((id,age))
            elif 'interests' in a:
                intersting += a[1]
            elif 'surname'in a:
                len_fam += len(a[1])
    return id_ages,intersting,len_fam

id_ages,intersting,len_fam= first_zadanie(students)
print('Список пар "ID студента — возраст":', id_ages)
print('Полный список интересов всех студентов:',intersting)
print('Общая длина всех фамилий студентов:',len_fam)

# TODO исправить код
