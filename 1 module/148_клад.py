test_string = '''
-2
9
вперёд
9
налево
вперёд
2
разворот
вперёд
17
стоп
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

treasure_x = int(input())
treasure_y = int(input())
x, y = 0, 0
current_direction = 0
command_count = 0

while True:

    command = input()
    command_count += 1

    if command == "вперёд":
        steps = int(input())
        if current_direction == 0:
            y += steps
        elif current_direction == 1:
            y -= steps
        elif current_direction == 2:
            x += steps
        elif current_direction == 3:
            x -= steps
    elif command == "налево":
        current_direction = (current_direction - 1) % 4
    elif command == "направо":
        current_direction = (current_direction + 1) % 4
    elif command == "разворот":
        current_direction = (current_direction + 2) % 4
    elif command == "стоп":
        break

    if x == treasure_x and y == treasure_y:
        break

print(command_count)
if current_direction == 0:
    print("север")
elif current_direction == 1:
    print("восток")
elif current_direction == 2:
    print("юг")
elif current_direction == 3:
    print("запад")
