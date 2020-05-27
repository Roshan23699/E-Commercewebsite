a = [2,4,5,6,12,16,17,20,21]
b = []

for i in range(1, 26):
	if i not in a:
		b.append(i)
print("Missing Page numbers :",b)
