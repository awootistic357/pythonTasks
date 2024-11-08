test_string = '''
3
5
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
number_1 = int(input())
number_2 = int(input())
print(number_1 + number_2)