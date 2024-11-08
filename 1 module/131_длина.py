test_string = '''
лоботомия
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

word_1 = input()
length = len(word_1)
print(f'Слово {word_1} имеет длину {length}')