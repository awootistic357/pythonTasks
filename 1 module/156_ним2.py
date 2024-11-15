test_string = '''
10
10
1
5
2
10
1
5
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

first = int(input())
second = int(input())

while (first != 0) or (second != 0):
    num = int(input())
    if num == 1:
        k = int(input())
        first -= k
        print(first, second)
    elif num == 2:
        f = int(input())
        second -= f
        print(first, second)