test_string = '''
15
10
.
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

column = int(input())
line = int(input())
symbol = input()
print(symbol * line)
for i in range(1, column - 2):
    print(symbol, ' ' * (line - 2), symbol, sep='')
print(symbol * line)
