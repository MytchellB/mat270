# Mytchell Beaton

import random
import matplotlib.pyplot as night1
import matplotlib.pyplot as night2
import matplotlib.pyplot as night3
import matplotlib.pyplot as night4
from matplotlib.markers import MarkerStyle

grid = [[0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9]] # Create our 10x10 grid as a 2d array.
myHouse = [[random.randint(0,9)], [random.randint(0,9)]] # Randomly choose the location where our house is.
print ("My House: ", myHouse)
bombHits = []
bombHitsHouseTotal = 0
nightCounter = 1

def dropBombs(): # Drops 200 bombs on 10x10 grid.
    global grid, myHouse, bombHits, bombHitsHouseTotal, nightCounter
    bombsHitHouse = 0
    i=0
    while(i<200):
        bombHit = [[random.randint(0,9)], [random.randint(0,9)]] # Randomly choose the location where a bomb hits.
        bombHits.append(bombHit) # Add the location to our array
        
        if(nightCounter == 1): # Plot the bomb hits on a graph and print out for each night.
            night1.scatter(bombHit[0], bombHit[1])
            night1.scatter(myHouse[0], myHouse[1], marker="*", label="My House")
            if(i == 199):
                night1.grid(color='black', linestyle='-', linewidth=1)
                night1.title("Night 1")
                night1.show()
        
        if(nightCounter == 2): # Plot the bomb hits on a graph and print out for each night.
            night2.scatter(bombHit[0], bombHit[1])
            night2.scatter(myHouse[0], myHouse[1], marker="*", label="My House")
            if(i == 199):
                night2.grid(color='black', linestyle='-', linewidth=1)
                night2.title("Night 2")
                night2.show()
                
        if(nightCounter == 3): # Plot the bomb hits on a graph and print out for each night.
            night3.scatter(bombHit[0], bombHit[1])
            night3.scatter(myHouse[0], myHouse[1], marker="*", label="My House")
            if(i == 199):
                night3.grid(color='black', linestyle='-', linewidth=1)
                night3.title("Night 3")
                night3.show()
        
        if(nightCounter == 4): # Plot the bomb hits on a graph and print out for each night.
            night4.scatter(bombHit[0], bombHit[1])
            night4.scatter(myHouse[0], myHouse[1], marker="*", label="My House")
            if(i == 199):
                night4.grid(color='black', linestyle='-', linewidth=1)
                night4.title("Night 4")
                night4.show()
    
        print ("Bomb #", i+1, " Hits: ", bombHit)
        if(bombHit == myHouse):
            print ("Bomb hit House!")
            bombsHitHouse += 1 # Increment our single night house hit counter
            bombHitsHouseTotal += 1 # Increment our total house hit counter
        i += 1
    print ("Number of bombs that hit house: ", bombsHitHouse, "\n")
    
def fourNights():
    global nightCounter
    i=0
    while(i < 4):
        dropBombs()
        nightCounter += 1
        i += 1
    return 0
    


fourNights()
print ("At the end of 4 nights, {} bombs hit my house, and # hits any grid could receive any night: ".format(bombHitsHouseTotal))

# night1.ylabel("Number of Tosses")
# night1.xlabel("Experiment Number")