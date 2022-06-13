import random


def printTable(tableDict):
    try:
        return "+-+-+-+ \n" \
               f"|{tableDict['A1']}|{tableDict['A2']}|{tableDict['A3']}| \n" \
               "+-+-+-+ \n" \
               f"|{tableDict['B1']}|{tableDict['B2']}|{tableDict['B3']}| \n" \
               "+-+-+-+ \n" \
               f"|{tableDict['C1']}|{tableDict['C2']}|{tableDict['C3']}| \n" \
               "+-+-+-+"
    except Exception as e:
        print(e)
        return 'wrong input'


def setupBombs(numOfBombs):
    if isinstance(numOfBombs, int):
        possibleBombs = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        bombPlacement = []
        if numOfBombs <= len(possibleBombs):
            for i in range(0, numOfBombs):
                bomb = random.choice(possibleBombs)
                possibleBombs.remove(bomb)
                bombPlacement.append(bomb)
            return bombPlacement
    return 'wrong input'


def decideIfBombOrPoints(coordinate, bombPlacement):
    if isinstance(coordinate, str) and isinstance(bombPlacement, list):
        return coordinate in bombPlacement
    return False


def decidePoints(coordinate, bombPlacement):
    bombPossiblities = {
        'A1': ['A2', 'B1', 'B2'],
        'A2': ['A1', 'A3', 'B1', 'B2', 'B3'],
        'A3': ['A2', 'B2', 'B3'],
        'B1': ['A1', 'A2', 'B2', 'C1', 'C2'],
        'B2': ['A1', 'A2', 'A3', 'B1', 'B3', 'C1', 'C2', 'C3'],
        'B3': ['A2', 'A3', 'B2', 'C2', 'C3'],
        'C1': ['B1', 'B2', 'C2'],
        'C2': ['B1', 'B2', 'B3', 'C1', 'C3'],
        'C3': ['B2', 'B3', 'C2']
    }
    return (len(list(set(bombPossiblities[coordinate]).intersection(bombPlacement))))


def game():
    viewedTable = {
        'A1': ' ', 'A2': ' ', 'A3': ' ',
        'B1': ' ', 'B2': ' ', 'B3': ' ',
        'C1': ' ', 'C2': ' ', 'C3': ' '
    }
    print(printTable(viewedTable))
    fullTable = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    bombPlacement = setupBombs(3)

    remainingPlaces = fullTable
    nonBomblist = [x for x in fullTable if (x not in bombPlacement)]

    gameRunning = True
    while gameRunning:
        choice = random.choice(remainingPlaces)
        remainingPlaces.remove(choice)

        print('choice: ', choice)

        if decideIfBombOrPoints(choice, bombPlacement):
            viewedTable[choice] = 'X'
            print(printTable(viewedTable))
            print('game Over bombs were at:', bombPlacement)
            gameRunning = False
        else:
            nonBomblist.remove(choice)
            viewedTable[choice] = decidePoints(choice, bombPlacement)
            print(printTable(viewedTable))
        if len(nonBomblist) == 0:
            print('You win')
            gameRunning = False

    return 'game end'


print(game())
