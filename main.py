import random
import matplotlib.pyplot as plt
import numpy as np
import SA1 as sa

#creates a list of items with unirandom values and weights, useful for testing algorithms
def unirandom_items(N):
    x = [None]*N
    x = [[random.uniform(0, 1), random.uniform(0, 1)] for item in x]
    return x


knapsack_size = 200 #maximum weight that the knapsack can hold
knapsack = [] #knapsacks initial contents
trajectory = [] #vector of solutions
weights = [] #vector of weights 

N = 1000 #iteration number

#creating a list of K items, size of each is its index, and value index squared
K = 101  #list size
x = [[index ** 2, index] for index in range(K)]


#swapping as many items as possible while assuring that an iteration can always be completed:
#maximum item size is 99 and the 2nd largest is 99, so knapsack sized 200 can hold at least 2 items
fixed_swap = 2

#calculating the exact analytical solution for this problem:
exact_solution = x[-1][0] + x[-2][0] + x[1][0] #= 19802


#initial knapsack fill
sa.fill(knapsack, x, knapsack_size)   

#creates unique knapsack, item list, weight vector, and trajectory for every algorithm
SAknapsack = [item for item in knapsack]
SAmodknapsack = [item for item in knapsack]
GSknapsack = [item for item in knapsack]
RSknapsack = [item for item in knapsack]

SAx = [item for item in x]
SAmodx = [item for item in x] 
GSx = [item for item in x]
RSx = [item for item in x]

SAmodvalue = sum([item[0] for item in SAmodknapsack])
SAvalue = sum([item[0] for item in SAknapsack])
GSvalue = sum([item[0] for item in GSknapsack])
RSvalue = sum([item[0] for item in RSknapsack])

SAweight = sum([item[1] for item in SAknapsack])
SAmodweight = sum([item[1] for item in SAmodknapsack])
GSweight = sum([item[1] for item in GSknapsack]) 
RSweight = sum([item[1] for item in RSknapsack])

SAweights = [item for item in weights]
SAmodweights = [item for item in weights]
GSweights = [item for item in weights]
RSweights = [item for item in weights]

SAtrajectory = [item for item in trajectory]
SAmodtrajectory = [item for item in trajectory]
GStrajectory = [item for item in trajectory]
RStrajectory = [item for item in trajectory]


#knapsacksize is also copied for every algorithm so it's easier to change their parameters w/ text replace
SAknapsack_size = knapsack_size
SAmodknapsack_size = knapsack_size
GSknapsack_size = knapsack_size
RSknapsack_size = knapsack_size
 
#creating storage space for best solution that each algorithm has found:
SAmod_best_solution = [item for item in SAmodknapsack]
SA_best_solution = [item for item in SAknapsack]
GS_best_solution = [item for item in GSknapsack]
RS_best_solution = [item for item in RSknapsack]


#resolution for the plots
plt.rcParams["figure.dpi"] = 360

#simulated annealing
SAtrajectory = []
T = 20000
a = 0.95

for i in range(N):
    SAtrajectory.append(SAvalue) #updating the vector of values
    SAweights.append(SAweight) #updating the vector of weights
    
    #defining activation function next step
    def Metro_fixed_T(fcurrent, fcandidate):
        global T
        return sa.Metropolis(fcurrent, fcandidate, T)
    
    new = sa.swap(SAknapsack, x, SAknapsack_size, Metro_fixed_T, n = fixed_swap)
    SAknapsack = new[0] #getting the knapsack state out of the step
    x = new[1] #getting the item list state out of the step
    
    SAvalue = sum([item[0] for item in SAknapsack]) #getting the SAknapsack's value
    SAweight = sum([item[1] for item in SAknapsack]) #getting the SAknapsack's weight
    
    #updating the best solution
    if SAvalue > sum([item[0] for item in SA_best_solution]): 
        SA_best_solution = [item for item in SAknapsack]
    
    T = a*T #updating the temperature
    
#drawing the trajectory    
plt.plot(range(len(SAtrajectory)), SAtrajectory,
         color = "red", linewidth = 2, linestyle = "--", label = "Classic SA")

#modified simulated annealing - greedy search but number of items redrawn lowers
SAmodtrajectory = []
T = 100000
a = 0.95

for i in range(N):
    SAmodtrajectory.append(SAmodvalue) 
    SAmodweights.append(SAmodweight)
    
    #this algorithm's trick: annealing the number of items drawn out with swap
    def func(T, knapsack):
        return round(len(knapsack) * np.exp(-1 / T))
    
    new = sa.swap(SAmodknapsack, x, SAmodknapsack_size, sa.GreedySearch, n = func(T, SAmodknapsack))
    SAmodknapsack = new[0]
    x = new[1] 
    SAmodvalue = sum([item[0] for item in SAmodknapsack])
    SAmodweight = sum([item[1] for item in SAmodknapsack]) 
    if SAmodvalue > sum([item[0] for item in SAmod_best_solution]): 
        SAmod_best_solution = [item for item in SAmodknapsack]
    
    T = a*T 

plt.plot(range(len(SAmodtrajectory)), SAmodtrajectory,
          color = "blue", linewidth = 2, linestyle = "-.", label = "Modified SA")

#greedy search
GStrajectory = []
for i in range(N):
    GStrajectory.append(GSvalue)
    weights.append(GSweight)
    new = sa.swap(GSknapsack, GSx, knapsack_size, sa.GreedySearch, n = fixed_swap)
    GSknapsack = new[0]
    GSx = new[1]
    GSvalue = sum([item[0] for item in GSknapsack])
    GSweight = sum([item[1] for item in GSknapsack])
    if GSvalue > sum([item[0] for item in GS_best_solution]): 
        GS_best_solution = [item for item in GSknapsack]
               
plt.plot(range(len(GStrajectory)), GStrajectory,
          color = "green", linewidth = 2, linestyle = ":", label = "GS")

#random search
RStrajectory = []
for i in range(N):
    RStrajectory.append(RSvalue)
    weights.append(RSweight)
    new = sa.swap(RSknapsack, RSx, knapsack_size, sa.RandomSearch, n = fixed_swap)
    RSknapsack = new[0]
    RSx = new[1]
    RSvalue = sum([item[0] for item in RSknapsack])
    RSweight = sum([item[1] for item in RSknapsack])
    if RSvalue > sum([item[0] for item in RS_best_solution]): 
        RS_best_solution = [item for item in RSknapsack]
            
plt.plot(range(len(RStrajectory)), RStrajectory,
          color = "gray", linewidth = 2, linestyle = "-", label = "RS")

#exact solution plot
plt.axhline(y = exact_solution, color = "black", linewidth = 2, label = "Exact solution")

#legend and axis titles
plt.legend(loc = "right")
plt.xlabel("Iteration")
plt.ylabel("Knapsack's value")

print("\nBest solution values\n")
print(f"GS: {round(sum([item[0] for item in GS_best_solution])/exact_solution, 3)}\n")
print(f"RS: {round(sum([item[0] for item in RS_best_solution])/exact_solution, 3)}\n")
print(f"SA: {round(sum([item[0] for item in SA_best_solution])/exact_solution, 3)}\n")
print(f"SAmod: {round(sum([item[0] for item in SAmod_best_solution])/exact_solution, 3)}\n")

