Feature: add bombs: 

    Scenario: select bomb placement 
        Given: new game 
        When: 1 bomb is needed to be placed
        Then: 1 coordinate is selected
    
    Scenario: select multiple bomb placement 
        Given: new game 
        When: multiple bomb is needed to be placed
        Then: multiple coordinate is selected
