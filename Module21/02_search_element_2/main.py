site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}
def find_key(struct,key):
	if key in struct:
		return struct[key]
	depth = input('Хотите ввести максимальную глубину? Y/N: ')
	if depth == 'y' or depth =='Y':
		user_depth = int(input('Введите максимальную глубину: '))
		for sub_struct in struct.values():
			if user_depth == 0:
				result = find_key(sub_struct,key)
				if result:
					break
			user_depth -= 1
		else:
			result = None
	else:
		for sub_struct in struct.values():
			if isinstance(sub_struct,dict):
				result = find_key(sub_struct,key)
				if result:
					break
		else:
			result = None
	return result
user_key = input('Введите искомый ключ: ')
value = find_key(site,user_key)
print('Значение ключа:',value)
