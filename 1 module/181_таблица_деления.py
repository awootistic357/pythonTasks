test_string = '''
3
2
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

k = int(input())
n = int(input())
for i in range(1, n+1):
    for j in range(1, k+1):
        print(j / i, sep='', end='\t')
    print()