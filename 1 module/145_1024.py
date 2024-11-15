test_string = '''
1024
1025
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
for i in range(2):
    n = int(input())
    m = 1
    i = 0
    while m <= n:
        if m==n:
            print(i)
            break
        else:
            m = m*2
            i = i+1
    if m > n:
        print("НЕТ!")