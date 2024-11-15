test_string = '''
парол
парол
пароль123
пароль123
пароль123
пароль124
'''[1:-1].split('\n')[::-1]

def input(prompt=''):
	if prompt:
		print(prompt)
	tmp = test_string.pop()
	print(f'input = {tmp}')
	return tmp

for i in range(3):
	password = input()
	checkpassword = input()

	if len(password) < 8:
		print('Пароль слишком короткий!')
	elif password != checkpassword:
		print('Пароли различаются!')
	else:
		print('OK')





