class Student:
    def __init__(self):
        self.Fi = input('Введите ФИ: ')
        self.group = int(input('Введите номер группы: '))
        self.score = list(map(int,input('Введите оценки через пробел: ').split()))
    def mid_score(self):
        return (sum(self.score))/len(self.score)
    def print_info(self):
        print(f'ФИ: {self.Fi}\nГруппа: {self.group}'
              f'\nОценки: {self.score}')

i = int(input('Введите количество студентов: '))
students,j = [],1
for x in range(i):
    students.append(Student())
students_list_sort = (sorted(students,key=lambda student: student.mid_score()))
for x in students_list_sort:
    print(f'\nСтудент_{j}')
    x.print_info()
    j += 1

