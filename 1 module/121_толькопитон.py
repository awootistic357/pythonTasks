test_string = '''
Python
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
word_1 = input()
if word_1 == 'Python':
    print('ДА')
else:
    print('НЕТ')