test_string = '''
5
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

num = int(input())
for i in range(0, num):
    space = ' ' * (num - i)
    symbols = '*' * (i * 2 + 1)
    print(space, symbols, space, sep='')