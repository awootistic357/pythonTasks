test_string = '''
2
4
1
1.3
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

width = float(input())
height = float(input())
depth = float(input())
waterSpeed = float(input())
whenFull = (width * height * depth) / waterSpeed

print(whenFull)