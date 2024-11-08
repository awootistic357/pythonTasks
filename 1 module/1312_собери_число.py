test_string = '''
777
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
number = int(input())
hundreds = number // 100
decades =  (number - hundreds * 100) // 10
single = number - (hundreds * 100) - (decades * 10)
firstEquation = hundreds + decades
secondEquation = decades + single
if firstEquation > secondEquation:
    print(f'{firstEquation}{secondEquation}')
else:
    print(f'{secondEquation}{firstEquation}')
