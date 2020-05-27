import math
i = 1
n = 0
while True:
	m = 0
	num = 0
	for j in range(1, i + 1):
		if i % j == 0:
			m += 1/j
			num += 1
	mean = num / m
	if round(mean,5).is_integer():
		print(i)
		n += 1
	if n == 10:
		break
	i += 1
