test_string = '''
12
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

w = 0
a = int(input())
for i in range(1, a + 1):
    if a % i == 0:
        w = w + 1
        print(i, end=" ")
print('\n', end='')
if w > 2:
    print("НЕТ")
else:
    print("ПРОСТОЕ")