test_string = '''
3
1
60
1
30
1
100
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

num, denum = 0, 1
n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    num = num * b + a * denum
    denum *= b

x, y = num, denum

while y > 0:
    x, y = y, x % y #НОД

print(num // x, '/', denum // x, sep='')