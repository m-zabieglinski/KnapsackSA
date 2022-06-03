# KnapsackSA
This repository contains 2 python files:
-SA1.py contains functions that allow to solve a knapsack problem using Simulated Annealing (SA)
-main.py uses those functions to solve a particular knapsack problem defined there and should be an example of how to employ SA1.py

**SA1.py** is built primarily on 2 functions:

**fill()** takes a knapsack and a list and fills the knapsack to the brim with items pulled out of the list at random: it takes a random item from the list,
if it fits into the knapsack, it's accepted, if it doesn't it's passed on and next item is randomly pulled, up until it has gone through the entire item list
**swap()** is based on fill(): it copies the given knapsack and list into a candidate solution. It pulls N random items out of the candidate knapsack and uses fill() on the candidate knapsack and candidate list to create a new candidate knapsack. If the 



![plot of solution trajectories for 4 different algorithms generated using SA1.py](![obraz](https://user-images.githubusercontent.com/100228539/171834981-fc340632-48bf-48c2-a1cd-a72604efcbdf.png))
