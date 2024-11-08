test_string = '''
192
189
145
162
172
!
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

minHeight = 150
maxHeight = 190
count = 0
smallest = 1000
biggest = 0


candidate = input()
while candidate != "!":
    height = int(candidate)
    if minHeight <= height <= maxHeight:
         count += 1
    if height < smallest:
        smallest = height
    if height > biggest:
        biggest = height
    candidate = input()

if count > 0:
    print(count)
    print(smallest, biggest)
else:
    print("Нет подходящих кандидатов.")
