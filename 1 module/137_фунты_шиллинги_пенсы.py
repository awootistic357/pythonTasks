test_string = '''
фартинг
204
пенс
100
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
for i in range(2):
    currency = input()
    numberOfCurrency = int(input())

    if (currency == 'фартинг'):
        sterlings = numberOfCurrency // 960
        shillings = (numberOfCurrency - sterlings * 960) // 48
        pences = (numberOfCurrency - (sterlings * 960) - (shillings * 48)) // 4
        if sterlings > 1:
            print(f'Фунтов: {sterlings}')

        if shillings > 1:
            print(f'Шиллингов: {shillings}')

        if pences > 1:
            print(f'Пенсов: {pences}')

    elif (currency == 'пенс'):
        sterlings = numberOfCurrency // 20
        shillings = (numberOfCurrency - sterlings * 20) // 12
        farthings = (numberOfCurrency - (sterlings * 20) - (shillings * 12)) * 4
        if sterlings > 1:
            print(f'Фунтов: {sterlings}')

        if shillings > 1:
            print(f'Шиллингов: {shillings}')

        if farthings > 1:
            print(f'Фартингов: {farthings}')
