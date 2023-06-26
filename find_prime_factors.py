def find_prime_factors(number: int):
	'''Takes in a positive integer, returns a list of its prime factors.'''
	factors = []
	prime_factors = []
	for denom in range(2, number + 1):
		if number % denom == 0:
			factors.append(denom)

	for num in factors:
		counter = 0
		for denom in range(2, num):
			if num%denom == 0:
				counter +=1
		if counter == 0:
			prime_factors.append(num)
	print(prime_factors)

number = int(input('Enter a positive number: '))
while number <= 0:
	print('Error: please enter a positive number: ')
	number = int(input())
find_prime_factors(number)