test_string = '''
5
12
19
3
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

for i in range(4):
    word_1 = int(input())
    if (5 <= word_1 <= 10) :
        print('УТРО')
    elif (11 <= word_1 <= 17):
        print('ДЕНЬ')
    elif (18 <= word_1 <= 22):
        print('ВЕЧЕР')
    elif (23 == word_1 or 0 <= word_1 <= 4):
        print('НОЧЬ')
    else:
        print('НЕКОРРЕКТНЫЙ ФОРМАТ')