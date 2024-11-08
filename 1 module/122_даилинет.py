test_string = '''
да
да
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
word_1 = input()
word_2 = input()
if word_1 == 'да' and word_2 == 'да' or word_1 == 'нет' and word_2 == 'нет':
    print('ВЕРНО')
else:
    print('НЕВЕРНО')