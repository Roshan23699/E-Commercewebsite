def sum_divisors(n):
	l = []
	for i in range(1, n // 2 + 1):
		if n % i == 0:
			l.append(i)
	return sum(l)
	
count = 0
for i in range(1, 100000):
	a = sum_divisors(i)
	b = sum_divisors(a)
	if a <= i:
		continue
	if b == i:
		print(i, "and", a)
		count += 1
	if count == 10:
		break
