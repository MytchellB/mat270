# Mytchell Beaton

import random

grid = [[0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9]] # Create our 10x10 grid as a 2d array.
myHouse = [[random.randint(0,9)], [random.randint(0,9)]] # Randomly choose the location where our house is.
print "My House: ", myHouse
bombHits = []
bombHitsHouseTotal = 0

def dropBombs(): # Drops 200 bombs on 10x10 grid.
    global grid, myHouse, bombHits, bombHitsHouseTotal
    bombsHitHouse = 0
    i=0
    while(i<200):
        bombHit = [[random.randint(0,9)], [random.randint(0,9)]] # Randomly choose the location where a bomb hits.
        bombHits.append(bombHit) # Add the location to our array
        print "Bomb #", i+1, " Hits: ", bombHit
        if(bombHit == myHouse):
            print "Bomb hit House!"
            bombsHitHouse += 1 # Increment our single night house hit counter
            bombHitsHouseTotal += 1 # Increment our total house hit counter
        i += 1
    print "Number of bombs that hit house: ", bombsHitHouse, "\n"
    
def fourNights():
    i=0
    while(i < 4):
        dropBombs()
        i += 1
    return 0
    


fourNights()
print "At the end of 4 nights, {} bombs hit my house, and # hits any grid could receive any night: ".format(bombHitsHouseTotal)