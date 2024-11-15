test_string = '''
11
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

rocks = int(input())
steps = 0

while rocks > 1:
    steps += 1 + rocks % 2
    rocks //= 2
print(steps)