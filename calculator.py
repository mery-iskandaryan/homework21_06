operator = 0
while operator != '5':
	operator = input('Enter the opeation you want to perform:\n1) +\n2) -\n3) *\n4) /\n5) Exit\n')
	if operator == '5':
		print('Thank you! Goodbye.')
		exit()	
	while operator not in ['1','2','3','4','5']:
			operator = input('Please enter one of the choicec above: ')	
	num1 = float(input('Enter the first number: '))
	num2 = float(input('Enter the second number: '))
	if operator == '1':
		sum = num1 + num2
		print(f'{num1} + {num2} = {sum}\n')
	elif operator == '2':
		dif = num1 - num2
		print(f'{num1} - {num2} = {dif}\n')
	elif operator == '3':
		mul = num1 * num2
		print(f'{num1} * {num2} = {mul}\n')
	elif operator == '4':
		while num2 == 0:
			print("Error: you can't divide by zero. Enter another number: ")
			num2 = float(input())
		div = num1 / num2
		print(f'{num1} / {num2} = {div}\n')


