import random

secretNumber = int(random.randint(1,20))
count = 0

try:
    for guess in range(1,7):
        guess = int(input('chose a number between 1 & 20: '))
        assert  guess >= 1 and guess <= 20
        count += 1
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break
    if guess == secretNumber:
        print('Good job! You guessed my number in '+str(count)+' attempts!')
    else:
        print('The number I was thinking of was: ',secretNumber)
except AssertionError:
    print('Number must be between 1 and 20')
