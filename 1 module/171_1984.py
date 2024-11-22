test_string = '''
6
С кем война?
С кем мир?
Меняем
С кем война?
Меняем
С кем война?
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

e = True
o = False
num = int(input())
for i in range(num):
    w = input()
    if w == 'С кем война?':
        if e:
            print('Евразия')
        else:
            print('Остазия')
    elif w == 'С кем мир?':
        if not o:
            print('Остазия')
        else:
            print('Евразия')
    else:
        e, o = o, e