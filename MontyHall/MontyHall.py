import random

def chooseWinningDoor(): # Chooses which door will have the car behind it.
    winningDoor = random.randint(0,2)
    return winningDoor
    
def chooseContestantsDoor(winningDoor): # chooses which door the contestant chooses.
    contestantsDoor = random.randint(0,2)
    return contestantsDoor
    
    
def montyOpensDoor(winningDoor, contestantsDoor): # Monty opens a losing door.
    montyDoor = 4
    if winningDoor == contestantsDoor and winningDoor == 0: # if contestant picked winning door.
        montyDoor = random.randint(1,2)
    elif winningDoor == contestantsDoor and winningDoor == 1: # if contestant picked winning door.
        montyDoor = random.randint(0,2)
        while(montyDoor == 1): # if we randomly generate the winning door, we will continue to generate random #'s until we don't select the winning door.
            montyDoor = random.randint(0,2)
    elif winningDoor == contestantsDoor and winningDoor == 2: # if contestant picked winning door.
        montyDoor = random.randint(0,1)
    elif winningDoor == 0 and contestantsDoor == 1:
        montyDoor = 2
    elif winningDoor == 0 and contestantsDoor == 2:
        montyDoor = 1
    elif winningDoor == 1 and contestantsDoor == 0:
        montyDoor = 2
    elif winningDoor == 1 and contestantsDoor == 2:
        montyDoor = 0
    elif winningDoor == 2 and contestantsDoor == 0:
        montyDoor = 1
    elif winningDoor == 2 and contestantsDoor == 1:
        montyDoor = 0
    
    print("Monty opens Door: {}".format(montyDoor))
    return montyDoor
    
numberSwitchWins = 0 # Keeps track of # of times contestant wins by switching the door they chose.
numberSwitchLosses = 0 # Keeps track of # of times contestant loses by switching the door they chose.

def ifSwitchWillWin(winningDoor, contestantsDoor, montyDoor): # discovers if contestant will win by changing which door they have selected.
    global numberSwitchLosses, numberSwitchWins
    if(winningDoor == contestantsDoor): # If the contestant already chose the winning door, than switching results in a Loss.
        print("Switching doors results in LOSS")
        numberSwitchWins += 1
    else:
        print("Switching doors results in WIN")
        numberSwitchLosses += 1
    return numberSwitchLosses, numberSwitchWins
        

i=0
while(i<1000): # loop as many times as needed.
    print("Trial #{}".format(i+1))
    winningDoor = chooseWinningDoor() # Randomly selects winning door with car behind it.
    contestantsDoor = chooseContestantsDoor(winningDoor) # Randomly selects the door the contestant chooses.
    print("Winning Door: {}".format(winningDoor))
    print("Contestants Door: {}".format(contestantsDoor))
    montyDoor = montyOpensDoor(winningDoor, contestantsDoor) # Monty opens a losing door.
    print("Num Wins / Num Losses: {} \n".format(ifSwitchWillWin(winningDoor, contestantsDoor, montyDoor)))
    i += 1