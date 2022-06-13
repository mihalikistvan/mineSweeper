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
   except:
      return 'wrong input'

def setupBombs(numOfBombs):
   if isinstance(numOfBombs, int):
      possibleBombs = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
      bombPlacement = []
      if numOfBombs <= len(possibleBombs):
         for i in range (0,numOfBombs):
            bomb = random.choice(possibleBombs)
            possibleBombs.remove(bomb)
            bombPlacement.append(bomb)
         return bombPlacement
   return 'wrong input'

def game(): 
   return "game end"  

