import random
a = int(input("Guess a number between 0 and 100\n"))
b = random.randint(0, 100)
i = 0
j = 100
while True:
    if a == b:
        print("You are correct")
        break
    elif a > b:
        print("The number is less than", a)
        j = a - 1
        a = int(input())
    else:
        print("The number is greater than", a)
        i = a + 1
        a = int(input())

            
