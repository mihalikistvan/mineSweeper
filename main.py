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

def game(): 
   return "game end"  

