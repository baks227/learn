age_dict = {
    ('Сидоров', 'Никита'): 35,
('Сидорова', 'Алина'): 34,
('Сидоров', 'Павел'): 10,
}

familya = input('Введите фамилию: ').lower()
for i_person in age_dict:
    if familya.lower() in i_person[0].lower() or familya+'а' in i_person[0].lower() \
            or familya[:len(familya)-1] in i_person[0].lower():
        print(i_person[0],i_person[1],age_dict[i_person])
