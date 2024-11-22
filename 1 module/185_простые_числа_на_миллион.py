test_string = '''
20
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

n = int(input())
k = 0

for i in range (1, n):
     for j in range (1, i + 1):
         if i % j == 0:
            k += 1
     if k == 2:
        print (i)
     k = 0