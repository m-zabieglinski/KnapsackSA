import random
import numpy as np

#fills sack to its limit, with items pulled at random from x
def fill(sack, x, knapsack_size):
    total_weight = sum([item[1] for item in sack])
    random.shuffle(x)
    for item in x:
        if item[1] < knapsack_size - total_weight:
            total_weight += item[1] #weight increase
            sack.append(item) #puts item in knapsack
            x.remove(item) #removes item from items
            
#takes n random items out of sack and fills the sack with new items from x
#x is then reappended with what we had taken out of the sack
#swap returns a list of 2 values: swap(sack, x)[0] is the resultant knapsack
#and swap(sack, x)[1] is the resultant item list
#takes a custom activation function
#lots of commented out prints that helped when debugging
def swap(sack, x, knapsack_size, activation, n = 1):
    
    rm_temp = random.sample(range(len(sack)), n) #indeces for items pulled out of sack
    temp = [sack[number] for number in rm_temp] #items to be pulled out of sack
    
    candidate_sack = [item for item in sack] #candidate solution
    candidate_items = [item for item in x] #remaining items list created by candidate solution
    
    # print("rm_temp")
    # print(rm_temp)
    # print("\ntemp")
    # print(temp)
    # print("\ncandidate_sack")
    # for item in candidate_sack:
    #     print(item)
    # print("\ncandidate_items")
    # for item in candidate_items:
    #     print(item)
  
    #pulling the items of out candidate_sack
    candidate_sack = [item for item in candidate_sack if item not in temp]

    fill(candidate_sack, candidate_items, knapsack_size) #filling candidate_sack and updating candidate_items
    
    # print("\ncandidate_sack")
    # for item in candidate_sack:
    #     print(item)
    # if random.random() <= activation(sum([item[0] for item in sack]), sum([item[0] for item in candidate_sack])):
    #     print("\nf aktywacji")
    #     print(activation(sum([item[0] for item in sack]), sum([item[0] for item in candidate_sack])))
    
    #updating solution if it passes the acceptance test
    if random.random() <= activation(sum([item[0] for item in sack]), sum([item[0] for item in candidate_sack])):
        for item in temp:
            candidate_items.append(item)
        return [candidate_sack, candidate_items]    
    else:
        return [sack, x]
    

#metropolis activation function
def Metropolis(fcurrent, fcandidate, T):
    return min(1, np.exp((fcandidate - fcurrent) / T))

#greedy search implementation
def GreedySearch(fcurrent, fcandidate):
    if fcurrent > fcandidate:
        return 0
    else:
        return 1

#random search implementation
def RandomSearch(fcurrent, fcandidate):
    return 1