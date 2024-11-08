test_string = '''
Железный человек
2
Восток
12:00
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

film_name = input()
chapter = input()
cinema_name = input()
time = input()

print(f'\nБилет на {film_name} {chapter} в {cinema_name} на {time} забронирован.')