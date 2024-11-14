test_string = '''
10
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

playerInput = int(input())
fib1 = 1
fib2 = 1
fib_sum = 0
print(fib1)
while fib_sum < playerInput:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print(fib1)