test_string = '''
560
100
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

subsidy = int(input())
livestock = int(input())

for bulls in range(1, subsidy // 20 + 1):
    for cows in range((subsidy - bulls * 20) // 10 + 1):
        calves = livestock - bulls - cows
        if bulls * 20 + cows * 10 + calves * 5 == subsidy:
            print(bulls, cows, calves)