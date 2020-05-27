import random
while True:
    a = input("Press r to roll a dice and q to quit\n")
    if a == 'r':
        b = random.randint(1, 6)
        print("Dice shows", b)
    elif a == 'q':
        break


