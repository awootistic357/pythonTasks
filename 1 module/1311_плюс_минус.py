test_string = '''
-0.52
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
number = float(input())
if number > 0:
    print('+')
elif number < 0:
    print('-')
else:
    print('0')