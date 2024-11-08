test_string = '''
5
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
word_1 = int(input())
if (5 <= word_1 <= 10) :
    print(-10 // 3, -10 % 3)
elif (11 <= word_1 <= 17):
    print('ДЕНЬ')
elif (18 <= word_1 <= 22):
    print('ВЕЧЕР')
elif (23 == word_1 or 0 <= word_1 <= 4):
    print('НОЧЬ')
else:
    print('НЕКОРРЕКТНЫЙ ФОРМАТ')