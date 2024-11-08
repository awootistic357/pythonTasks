test_string = '''
1337
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
total = 0
money = int(input())
while money > 8:
    money = money // 8
print(money)