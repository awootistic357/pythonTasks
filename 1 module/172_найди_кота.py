test_string = '''
4
Как устроен типичный фрукт:
кожура;
мякоть;
косточки.
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

count = 0
exitLoop = False
while not exitLoop:
    userString = input()
    if ('кот' in userString) or ('Кот' in userString):
        print('МЯУ')
        break