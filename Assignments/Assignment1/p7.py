print("Enter the range in which you want armstrong numbers")
i = input()
j = input()
s = 0
for a in range(int(i), int(j)):
    b  = []
    b = list(map(int, str(a)))
    sum = 0
    for m in b:
        sum  = sum + m ** len(b)
    if sum == a:
        print(a)
