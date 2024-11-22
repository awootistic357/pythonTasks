test_string = '''
3
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

n = int(input())
number = 1
for i in range(1, n + 1):
    for j in range(i):
        print("Осталось секунд:", (i - j) - 1)
    print("Пуск", i)