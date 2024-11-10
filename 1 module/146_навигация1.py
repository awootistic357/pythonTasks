test_string = '''
9
вперед
4
разворот
вперед
2
вперед
1
разворот
вперед
10
вперед
2
0
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

tunnel_length = int(input())
position = 0
direction = 1
i = 0

while True:
    command = input()
    if command == '0':
        break
    i += 1
    if command == 'вперед':
        steps = int(input())
        position += steps * direction
    elif command == 'разворот':
        direction *= -1

    if position >= tunnel_length:
        command = input()
        if command == '0':
            break
        if command == 'вперед':
            steps = int(input())
            position += steps * direction
        elif command == 'разворот':
            direction *= -1
        break

print(i)