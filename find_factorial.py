def find_factorial(x: int):
	fact = 1
	num = 1
	if x < 0:
		raise ValueError('Only positive numbers are allowed')
	elif x == 0:
		pass
	elif x == 1:
		print(fact)
	else:
		while num <= x:
			fact = fact * num
			num +=1
		print(fact)

x = int(input('Enter a number to calculate its factorial: \n'))
find_factorial(x)

		
		