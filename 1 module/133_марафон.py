test_string = '''
37
13
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

marathon = int(input())
speed = int(input())
days = (-marathon // speed)

print(-days)