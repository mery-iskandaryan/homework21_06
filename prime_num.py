primes = []
for num in range(2,100):
	for denom in range(2, num):
		if num % denom == 0:
			break
	else:
		primes.append(num)

print(primes)


