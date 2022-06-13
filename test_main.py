from main import * 

def test():
    #game
    assert game() == "game end"
    
    #table printing
    viewedTable0= ''
    viewedTable1= {
            'A1':' ','A2':' ','A3':' '
        }
    viewedTable2= {
        'A1':' ','A2':' ','A3':' ',
        'B1':' ','B2':' ','B3':' ',
        'C1':' ','C2':' ','C3':' '
    }
    viewedTable3= {
        'A1':'1','A2':'1','A3':'1',
        'B1':'1','B2':' ','B3':'1',
        'C1':'1','C2':'1','C3':'1'
    }
    assert printTable(viewedTable0) == 'wrong input'
    assert printTable(viewedTable1) == 'wrong input'
    assert printTable(viewedTable2) == "+-+-+-+ \n" \
                                        f"| | | | \n" \
                                        "+-+-+-+ \n" \
                                        f"| | | | \n" \
                                        "+-+-+-+ \n" \
                                        f"| | | | \n" \
                                        "+-+-+-+"
    assert printTable(viewedTable3) == "+-+-+-+ \n" \
                                        f"|1|1|1| \n" \
                                        "+-+-+-+ \n" \
                                        f"|1| |1| \n" \
                                        "+-+-+-+ \n" \
                                        f"|1|1|1| \n" \
                                        "+-+-+-+"