test_string = '''
1000
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

n = int(input())
a = 0
p = 3.141592653589793

for i in range(1, n + 1):
    a += 1 / (i ** 2)
print((p ** 2) / a)