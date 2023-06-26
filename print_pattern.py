def print_pattern(number):
	i = 1
	ls = []
	ls.append(i)
	while i <= number:
		print(ls)
		i += 1
		ls.append(i)

number = int(input('Enter a number: '))
print_pattern(number)