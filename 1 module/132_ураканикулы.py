test_string = '''
Пенза
Нижний Новгород
Тула
Тула
Тула
Пенза
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
for i in range(3):
	word_1 = input()
	word_2 = input()
	if (word_1 == 'Тула' or word_1 == 'Пенза') and (word_2 == 'Пенза' or word_2 == 'Тула'):
		print('НЕТ')
	elif (word_1 == 'Тула' or 'Пенза') or (word_2 == 'Тула' or 'Пенза'):
		print('ДА')