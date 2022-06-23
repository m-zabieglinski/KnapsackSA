# KnapsackSA
This repository contains 2 python files:

-SA1.py contains functions that allow to solve a knapsack problem using Simulated Annealing (SA)

-main.py uses those functions to solve a particular knapsack problem defined there and should be an example of how to employ SA1.py


**SA1.py** is built primarily on 2 functions:

**fill()** takes a knapsack and a list and fills the knapsack to the brim with items pulled out of the list at random: it takes a random item from the list,
if it fits into the knapsack, it's accepted, if it doesn't it's passed on and next item is randomly pulled, up until it has gone through the entire item list

**swap()** is based on fill(): it copies the given knapsack and list into a candidate solution. It pulls N random items out of the candidate knapsack and uses fill() on the candidate knapsack and candidate list, creating 2 new objects. If the candidate knapsack passes the activation function's test (for example, if the candidate's value is greater than the current knapsack's value, which would be Greedy Search), then swap() returns the candidate. If not, swap() returns the knapsack and the item list that were used as its argument (acts an identity function).

SA1.py also contains 3 activation functions:

**GreedySearch()** which performs a greedy search (only accepts better solutions when swapping)

**RandomSearch()** which performs a random search (accepts every solution when swapping)

**Metropolis()** which is the Metropolis activation function: it always accepts a better solution and accepts a worse solution with some probability, which is a function of temperature parameter

Metropolis() is what enables the algorithm to work as Simulated Annealing (SA)

main.py compares 4 different search algorithm based on SA1.py, example trajectory of which is displayed below as a plot. Notice that the SA algorithm does not outperform GS. Perhaps the stohastic nature of fill() and swap() protects the GS implementation against its biggest enemy: the local minimum trap.



![plot of solution trajectories for 4 different algorithms generated using SA1.py](https://user-images.githubusercontent.com/100228539/171834981-fc340632-48bf-48c2-a1cd-a72604efcbdf.png)
