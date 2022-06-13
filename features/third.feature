Feature: decide if bomb: 

    Scenario: placement is given
        Given: bomb placement, coordinate
        When: given coordinate is bomb
        Then: bomb is activated end of game
    
    Scenario: placement is given
        Given: bomb placement, coordinate
        When: given coordinate is not bomb
        Then: points calculated for coordinate
