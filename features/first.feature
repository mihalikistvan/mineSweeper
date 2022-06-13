Feature: viewable gametable: 

    Scenario: Print an empty board 
        Given: new game 
        When: an empty board is created
        Then: the board is printed
    
    Scenario: Print a board with populated tries 
        Given: game is running 
        When: at least 1 step is allready done 
        Then: the board is printed with the populated records
