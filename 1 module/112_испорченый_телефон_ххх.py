test_string = '''
И мне, и жене, и Тотоше.
Мой милый, хороший,
Пришли мне калоши,
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

third_str = input()
first_str = input()
second_str = input()

print(first_str + '\n' + second_str + '\n' + third_str)