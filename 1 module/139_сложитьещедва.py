test_string = '''
13.37
177.013
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
number_1 = float(input())
number_2 = float(input())
print(number_1 + number_2)