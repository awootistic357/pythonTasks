test_string = '''
2
1
вперед
2
разворот
вперед
1
0
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

tunnel_length = int(input())
positionOfRoach = int(input())
direction = 1
i = 0

while True:
    command = input()
    if command == '0':
        break
    i += 1
    if command == 'вперед':
        steps = int(input())
        positionOfRoach = positionOfRoach +  (steps * direction)
    elif command == 'разворот':
        direction *= -1

    if (positionOfRoach >= tunnel_length) or (positionOfRoach <= -1):
        command = input()
        if command == '0':
            break
        if command == 'вперед':
            steps = int(input())
            positionOfRoach = positionOfRoach + (steps * direction)
        elif command == 'разворот':
            direction *= -1
        break
print(i)
if positionOfRoach >= tunnel_length:
    print('справа')
elif positionOfRoach <= -1:
    print('слева')