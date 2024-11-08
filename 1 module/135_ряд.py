test_string = '''
1
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

number = float(input()) #1 шаг

nextN = number + 1
number = nextN + number
nextN = nextN + 1
number = number * nextN
number = number + (nextN+1)
nextN = nextN + 1
number = number * (nextN+1)
nextN = nextN + 1
number = number + (nextN+1)
nextN = nextN + 1
number = number * (nextN+1)
nextN = nextN + 1
number = number + (nextN+1)
nextN = nextN + 1
number = number * (nextN+1)
print(number)