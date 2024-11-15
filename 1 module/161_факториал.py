test_string = '''
4
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

n = int(input())
number = 0
factorial = 1

for n in range(n):
    number += 1
    factorial = factorial * number

print(factorial)