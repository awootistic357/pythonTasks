test_string = '''
2
3
470
430
465
2
451
450
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

number = int(input())
maximum = 0
road = 1

for element in range(number):
    tunnel = int(input())
    m = 100000000
    for element_2 in range(tunnel):
        height = int(input())
        if m > height:
            m = height
    if maximum < m:
        maximum = m
        road = element + 1

print(road, maximum)