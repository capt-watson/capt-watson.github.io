import random
import sys

wins = 0
losses = 0
ties = 0

try:
    while True:
        print('wins= %s, losses= %s, tie= %s' % (wins, losses, ties))     
        playerMove = input('Enter your move: (r)Rock, (s)Scissors, (p)Paper or (q)Quit:  ')
        if playerMove not in ['r','s','p','q']:
            print('Please enter only characters from:  r  p  s  q')
        if playerMove == 'r':
            print('ROCK Versus... ')
        elif playerMove == 's':
            print('SCISSORS Versus... ')
        elif playerMove == 'p':
            print('PAPER Versus... ')
        randomNumber = random.randint(1,3)
        if randomNumber == 1:
            computerMove = 'r'
            print('Rock')
        elif randomNumber == 2:
            computerMove = 's'
            print('Scissors')
        elif randomNumber == 3:
            computerMove = 'p'
            print('Paper')
        if playerMove == computerMove:
            print('It is a tie!')
            ties = ties + 1
        elif playerMove == 'r' and computerMove == 's':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'p' and computerMove == 'r':
            print('You win!')
            wins = wins + 1
        elif playerMove == 's' and computerMove == 'p':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'r' and computerMove == 'p':
            print('You lose!')
            losses = losses + 1
        elif playerMove == 'p' and computerMove == 's':
            print('You lose!')
            losses = losses + 1
        elif playerMove == 's' and computerMove == 'r':
            print('You lose!')
            losses = losses + 1
        if playerMove == 'q':
            print('You typed quit.')
            sys.exit()
except SystemExit:
    print('You have exited the game')