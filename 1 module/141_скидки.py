test_string = '''
1337
52
2390
150
-1
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
total = 0
print('Вводите цены; для остановки введите -1.')
price = float(input())
while price > 0:
    if price > 1000:
        sale = price * 0.005
        price -= sale
    total += price
    price = float(input())
print('Общая стоимость равна', round(total, 2))