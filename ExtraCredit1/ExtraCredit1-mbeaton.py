import random

def flipUntilHeads():
    foundHeads = False
    numFlipsUntilHeads = 0
    while ( foundHeads == False):
        numFlipsUntilHeads += 1
        if random.randint(0,2) == 0:
            foundHeads = True
            return numFlipsUntilHeads
            

totalTimesCoinFunctionRun = 0
currentResult = 0
numEvenResults = 0
numOddResults = 0
while totalTimesCoinFunctionRun < 1000:
    currentResult = flipUntilHeads()
    totalTimesCoinFunctionRun += 1
    if ( currentResult % 2 == 0 ):
        numEvenResults += 1
        print("Result is even ")
    else:
        numOddResults += 1
        print("Result is odd ")
    print("{} number of times run: {}".format(currentResult, totalTimesCoinFunctionRun))
    
print "number of even Results: {}".format(numEvenResults) 
print "number of odd Results: {}".format(numOddResults)