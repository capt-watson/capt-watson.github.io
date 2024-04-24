import random
import time
import copy

WIDTH = 60
HEIGHT = 20

#! Create a list for the cells

nextCells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  ## Add a living cell
        else:
            column.append(' ')  ## Add a dead cell
    nextCells.append(column)    ## nextCells is a list of column list
    
while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)  ## separate each step with a new line
    for y in range(HEIGHT):                  ## print currentCells on the screen.
        for x in range(WIDTH):
            print(currentCells[x][y], end='') ## print the # or space
        print()                               ## print a new line at the end of the row
        
## calculate the next step's cells based on current step's cells

    for x in range(WIDTH):         ## get neighboring coordinates
        for y in range(HEIGHT):    ## '% WIDTH' ensures leftCoord is always between 0 and WIDTH - 1 
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

## count number of living neighbors

            numNeighbors = 0

            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1       ## Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1       ## Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1       ## Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1       ## Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1       ## Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1       ## Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1       ## Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1       ## Bottom-right neighbor is alive.

## set cell based on Conway's Game of Life rules

            ## living cell with 2 or 3 neighbors stay alive
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'

            ## dead cells with 3 neighbors become alive
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'

            ## everything else dies or stays dead
            else:
                nextCells[x][y] = ' '

## add a 1 second pause to reduce flickering

    time.sleep(1)
