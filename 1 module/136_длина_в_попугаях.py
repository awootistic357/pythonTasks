test_string = '''
Хотите шутку про альцгеймер? Хотите шутку про альцгеймер? Хотите шутку про альцгеймер?
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

userString = input()
length = len(userString)
parrotsFitIn = length // 6
print(parrotsFitIn)