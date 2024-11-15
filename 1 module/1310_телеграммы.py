test_string = '''
съешь ещё этих мягких французских булок, да выпей чаю
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
userString = input()
length = len(userString)
valuePerSymbol = length * 40 #цена в копейках
rubles = valuePerSymbol // 100.00
kopeck = valuePerSymbol % 100
print(f'{int(rubles)} р. {kopeck} коп.')
