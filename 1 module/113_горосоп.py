test_string = '''
Иван
Кузнецов
лис
овен
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

name = input()
forname = input()
animal = input()
sign = input()

print(f'''
Индивидуальный гороскоп для пользователя {name} {forname}
Кем вы были в прошлой жизни: {animal}
Ваш знак зодиака - {sign}, поэтому вы - тонко чувствующая натура.''')