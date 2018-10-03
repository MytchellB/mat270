
# Title: darts_probability.py
# Description: Numerical experiment that simulates the outcome of randomly throwing a dart(s) at a circular dartboard of unit radius.
# Author: Mytchell Beaton
# Date: 9/25/18
#
import matplotlib.pyplot as plt
import numpy as np 


 
# ---
# --- randomly generate location of a specified number of darts (random points in circle)
# ---
def randomDarts(num_darts=10,showPlot=1):
    x = []     # array for x-coordinates of dart(s) location
    y = []     # array for y-coordinates of dart(s) location
    countSuccess = 0    # counter for how many darts land in a given subregion of dart board
    
    # Begin throwing random darts
    for j in range(num_darts):        
        
        r = np.sqrt(np.random.rand())    # generate random radius in [0,1) -- Note: We use square root of random number since in Cartesian coordinates we use radius^2 where as polar coordinates we simply use the radius.  Without the square root the results in Cartesian points grouped more near the center of circle.
        Theta = 2*np.pi *np.random.rand()   # generate random angle in [0,2pi)
        x.append(1 * r * np.cos(Theta))   # x-coordinate of new random point
        y.append(1 * r* np.sin(Theta))   # y-coordinate of new random point
        countSuccess += inRegion(x[j],y[j])  # check if point is in our region
    if showPlot==1:    # plot diamond/square
        plotResults(x,y)
        
    return (x,y,countSuccess)

# ---
# --- Determine if dart landed in a specified region   
# ---    
def inRegion(x,y):
    # Consider the region inside the unit circle but outside the unit "diamond" (i.e. unit (1-norm) ball)
    vec=[x,y]
    if np.linalg.norm(vec,1)>=1:
        return 1    # outside diamond but inside circle
    else:
        return 0    # inside diamond
    
# ---
# --- Plotting / Display Results
# ---
def plotResults(x,y):
    plt.figure()
    
    # plot outcome of each dart
    plt.plot([x], [y],marker='o',color='r',markersize=4)  # plot location of darts as points
    plt.ylim([-1.25,1.25])     # y-axis plot limits 
    plt.xlim([-1.25,1.25])   # x-axis plot limits 
     
    # plot unit circle
    theta = np.linspace(0, 2*np.pi, 1000) # Create equally spaced points between 0 and 2pi
    plt.plot(np.cos(theta), np.sin(theta))     
    
    # plot "diamond" or l^1 unit ball
    xR = np.linspace(0,1,1000)     # Create equally spaced points between 0 and 1
    xL = np.linspace(-1,0,1000)     # Create equally spaced points between -1 and 0
    l1 = -xR+1    # line 1: y = -x +1
    l2 = xR-1       # line 2: y = x-1
    l3 = xL+1    # line 3: y=x+1
    l4 = -xL-1   # line 4 : y=-x-1
    plt.plot(xR,l1,color='b',linestyle='dashed')
    plt.plot(xR,l2,color='b',linestyle='dashed')
    plt.plot(xL,l3,color='b',linestyle='dashed')
    plt.plot(xL,l4,color='b',linestyle='dashed')
 
    plt.grid()    # Show grid
    
    
    plt.show() # display plot(s)


# ---
# --- Run experiments  
# ---        

# !!! Single Experiment

num_darts = 100   # How many darts to be thrown
countSuc = 0
[x,y,countSuc]=randomDarts(num_darts)  # Throw the darts
print('%s out of %s  darts landed in region. The observed probability is %s  ' % (countSuc,num_darts,float(countSuc)/float(num_darts)) )

# !!! Multiple Experiments with increasing number of darts being thrown
for j in range(1,5):
    num_darts = j*10
    [x,y,countSuc]=randomDarts(num_darts,0)
    print('%s out of %s  darts landed in region. The observed probability is %s  ' % (countSuc,num_darts,float(countSuc)/float(num_darts)) )
    
# !!! Multiple Experiments with same number of darts thrown
numExper = 1000
experResults=[]

for j in range(0,numExper):
    num_darts = 10
    [x,y,countSuc]=randomDarts(num_darts,0)
    experResults.append(float(countSuc)/float(num_darts))
    

print(' ---------------------------------------------')
print('The theoretical prediction of the probability is (Pi-2)/Pi approx  %f' % float((np.pi -2)/np.pi))
print('From %s experiments of throwing %s darts, the average probability of success is %s' % (numExper, num_darts, np.mean(experResults)))
print(' ---------------------------------------------')
