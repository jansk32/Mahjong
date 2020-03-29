from enum import Enum

valCounts = [1,2,3,4,5,6,7,8,9]
wind = [4,5,6,7]
dragon = [8,9,10]

class Suite(Enum):
    # NORMAL SUITES
    BAMBOO = 1
    DOTS = 2
    HORSE = 3
    
    # WIND
    NORTH = 4
    EAST = 5
    SOUTH = 6
    WEST = 7

    # DRAGONS
    RED = 8
    GREEN = 9
    WINDOW = 10

    # FLOWER
    FLOWER = 11