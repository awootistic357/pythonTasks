test_string = '''
12
9
2012
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

d = int(input())
m = int(input())

m -= 2

k = int(input())

c = k // 100
y = k % 100

print((d + (((13 * m) - 1) // 5) + y + ((y // 4) + c // 4 - (2 * c) + 777)) % 7)