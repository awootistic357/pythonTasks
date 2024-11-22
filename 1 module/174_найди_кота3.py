test_string = '''
Как устроен типичный фрукт:
кожура;
мякоть;
косточки.
СТОП
Как устроен обычный человек:
кожа;
мышцы;
кости;
органы.
СТОП
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

for i in range(2):
    count = 0
    cats = 0
    h = 0
    exitLoop = False
    userString = ''
    while userString != 'СТОП':
        userString = input()
        count +=1
        if ('кот' in userString) or ('Кот' in userString):
            if exitLoop != True:
                h = count
            exitLoop = True
            cats += 1
    if h == 0:
        print(cats, -1)
    else:
        print(cats, h)