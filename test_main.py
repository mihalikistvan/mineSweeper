from main import * 

def test():
    ### game
    assert game() == "game end"
    
    ### table printing
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

    ### bomb setup
    setup0 =setupBombs('testForWrongInput')
    setup1 =setupBombs(1)
    setup2 =setupBombs(3)
    setup3 =setupBombs(8)
    setup4 =setupBombs(12)

    assert setup0  == 'wrong input'
    assert len(setup1)  == 1
    assert len(setup2)  == 3
    assert len(setup2)  == len(set(setup2))
    assert len(setup3)  == 8
    assert len(setup3)  == len(set(setup3))
    assert setup4  == 'wrong input'

    ### point system
    assert decideIfBombOrPoints('A2',['A2','B1','B2']) == True
    assert decideIfBombOrPoints('A1',['A2','B1','B2']) == False
    assert decideIfBombOrPoints('A1',[]) == False
    assert decideIfBombOrPoints(12,['A2','B1','B2']) == False
    assert decideIfBombOrPoints('A2',['A2']) == True

    assert decidePoints('A1',['A2','B1','B2']) == 3
    assert decidePoints('A2',['C1','C2','C3']) == 0
    assert decidePoints('B2',['A1','C2','C3']) == 3
    assert decidePoints('B2',['C1','C2','C3']) == 3
