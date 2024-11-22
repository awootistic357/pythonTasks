test_string = '''
5
6122802
14406496
15230209
2541121
1758741
5
1865535
13479687
16689153
1839958
5214020
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

for i in range(2):
    lastHash = 0
    for i in range(int(input())):
        block = int(input())
        currentHash = block % 256 # "первый разряд" от умножения на 256
        r = (block // 256) % 256 # "средний разряд" от умножения на 256
        m = block // 256 ** 2 # "крайний разряд" от умножения на 256
        calcHash = (37 * (m + r + lastHash)) % 256 # хеш по формуле
        if calcHash != currentHash or calcHash > 100:
            print(i)
            break
        lastHash = calcHash
    else:
        print(-1)