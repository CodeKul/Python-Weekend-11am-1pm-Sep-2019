import random

while True:
    no1 = int(input('Enter a number between 1-10: '))
    if no1 == 0:
        print('Bye!')
        break
    elif no1 < 1 or no1 > 10:
        print('Invalid input')
        continue
    no2 = random.randint(1, 10)

    if no1 == no2:
        print('You won!')
    else:
        print('Better luck next time!')