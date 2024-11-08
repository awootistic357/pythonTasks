test_string = '''
122
111
124
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp
height1 = int(input())
height2 = int(input())
height3 = int(input())
temporaryslot = 0
if height2 > height3:
    height2 = height3
    height3 = height2
else:
    temporaryslot = height2
    height2 = height3
    height3 = temporaryslot
if height1 < height2:
    temporaryslot = height1
    height1 = height2
    height2 = temporaryslot
print(f'{height1}\n{height2}\n{height3}')