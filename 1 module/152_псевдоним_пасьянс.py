test_string = '''
10
1
1
5
3
2
4
4
3
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

rocks = int(input())

while rocks > 0:
    playerSteps = int(input())
    if (playerSteps < 0) or (playerSteps > 3) or (playerSteps > rocks):
        print(rocks)
    else:
        rocks -= playerSteps
        print(rocks)