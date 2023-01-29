from random import *
import time as t
from pygame import *
# Completed by Lukas L-A 12Be


def buildGameGrid(grid):
    for x in range(101):
        for i in range(101):
            randCurr = randint(1, 3)
            if randCurr == 1:  # or randCurr == 4 or randCurr == 7:
                grid[x][i] = 1
            else:
                grid[x][i] = 0

    return grid


def printGrid(grid):
    for x in range(100):
        print(grid[x])


def drawGrid(grid):
    screen.fill((255, 255, 255))
    y_offset = 0
    row = 0
    while row < 100:
        x_offset = 0
        col = 0
        while col < 100:
            if grid[row][col] == 1:
                draw.rect(screen, (0, 0, 0), (10 * x_offset + 10, 10 * y_offset + 10, 5, 5))
            else:
                draw.rect(screen, (128, 128, 128), (10 * x_offset + 10, 10 * y_offset + 10, 5, 5))

            x_offset += 1
            col += 1
        y_offset += 1
        row += 1



def checkNeighbours(grid, gameGrid):
    for y in range(101):
        for x in range(101):
            currentAlive = 0
            if x < 100 and grid[y][x + 1] == 1:
                currentAlive += 1
            if x > -1 and grid[y][x - 1] == 1:
                currentAlive += 1
            if y > -1 and grid[y - 1][x] == 1:
                currentAlive += 1
            if y < 100 and grid[y + 1][x] == 1:
                currentAlive += 1
            if x < 100 and y < 100 and grid[y + 1][x + 1] == 1:
                currentAlive += 1
            if x > -1 and y > -1 and grid[y - 1][x - 1] == 1:
                currentAlive += 1
            if y > -1 and x < 100 and grid[y - 1][x + 1] == 1:
                currentAlive += 1
            if y < 100 and x > -1 and grid[y + 1][x - 1] == 1:
                currentAlive += 1

            if currentAlive < 2:
                gameGrid[y][x] = 0
            if currentAlive == 2 and grid[y][x] == 1:
                gameGrid[y][x] = 1
            if currentAlive == 3:
                gameGrid[y][x] = 1
            if currentAlive > 3:
                gameGrid[y][x] = 0

    grid = gameGrid

    return grid, gameGrid


if __name__ == '__main__':
    backGrid = [[None for i in range(101)] for x in range(101)]
    backGrid = buildGameGrid(backGrid)
    printGrid(backGrid)
    displayGrid = backGrid

    init()
    width = 1000
    height = 1000

    screen = display.set_mode((width, height))

    while True:
        for e in event.get():
            if e.type == QUIT:
                exit()
        backGrid, displayGrid = checkNeighbours(backGrid, displayGrid)
        printGrid(displayGrid)
        drawGrid(displayGrid)
        display.flip()
        t.sleep(0.5)