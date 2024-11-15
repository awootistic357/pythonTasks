test_string = '''
15.9
16.3
16.8
19.1
20.5
20.1
21.8
22.4
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

temp = float(input())

days = 0

while temp < 22.0:
    days += 1
    temp = float(input())

print(days // 7)