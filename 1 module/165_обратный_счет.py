test_string = '''
5
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

n = int(input())

if n >= 0:
    print('Осталось секунд:', n)
    for i in range(n):
        n -= 1
        print('Осталось секунд:', n)
    print('Пуск')
else:
    print('Пуск')