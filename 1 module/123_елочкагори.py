print('Начните отсчёт до трёх, чтобы ёлочка загорелась')
test_string = '''
раз
два
три
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
word_1 = input()
word_2 = input()
word_3 = input()
if word_1 == 'раз' and word_2 == 'два' and word_3 == 'три':
    print('ГОРИ')
else:
    print('НЕ ГОРИ')