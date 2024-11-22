test_string = '''
32
30
31
34
38
37
39
0
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

price1 = int(input())
price2 = int(input())
in_stock = False
while price2 != 0:
    if in_stock == False:
        if price1 < price2:
            bought= price2
            in_stock = True
    if in_stock == True:
        if price1 > price2:
            sold = price2
            break
    price1 = price2
    price2 = int(input())

print(bought, sold, sold - bought)