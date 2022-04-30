import random
import time


def checkDead(x, y):
    count = -1
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 < i < len(board) and 0 < j < len(board[i]):
                if board[i][j] == "#":
                    count += 1
    if count == 2 or count == 3:
        return False
    return True


def checkAlive(x, y):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 < i < len(board) and 0 < j < len(board[i]):
                if board[i][j] == "#":
                    count += 1
    if count == 3:
        return True
    return False


def oneTurn():
    turnAlive = []
    turnDead = []

    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            if board[r][c] == "#" and checkDead(r, c):
                turnDead.append(r)
                turnDead.append(c)
            elif board[r][c] == " " and checkAlive(r, c):
                turnAlive.append(r)
                turnAlive.append(c)

    for x in range(0, len(turnAlive), 2):
        board[turnAlive[x]][turnAlive[x + 1]] = "#"

    for x in range(0, len(turnDead), 2):
        board[turnDead[x]][turnDead[x + 1]] = " "

    printBoard()
    print("=" * (len(board[0]) * 2 - 1))


def printBoard():
    for x in board:
        for y in x:
            print(y, end=" ")
        print()


def createBoard(x, y):
    board = []
    for i in range(x):
        temp = []
        for j in range(y):
            rand = random.randint(0, 1)
            if rand > 0.5:
                temp.append(" ")
            else:
                temp.append("#")
        board.append(temp)

    return board


'''board = [[" ", " ", " ", " ", " ", " "],
         [" ", " ", "#", " ", " ", " "],
         [" ", " ", " ", "#", " ", " "],
         [" ", "#", "#", "#", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "]]'''

board = createBoard(6, 6)

printBoard()
print("=" * (len(board[0]) * 2 - 1))
while True:
    oneTurn()
    time.sleep(1)
