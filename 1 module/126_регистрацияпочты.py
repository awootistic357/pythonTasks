test_string = '''
S.L.Jackson
MEGAKILLE@Rexample.com
S.L.Jackson
MEGAKILLERexample.com
S.L.@Jackson
MEGAKILLE@Rexample.com
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

	if '@' not in word_1 and '@' in word_2:
		print('ОК')
	elif '@' not in word_2:
		print('НЕКОРРЕКТНЫЙ АДРЕС')
	else:
		print('НЕКОРРЕКТНЫЙ ЛОГИН')