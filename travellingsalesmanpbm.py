# Travelling Salesman Problem - Simple Approach Implementation in Python  
  
# importing the required modules  
from itertools import permutations  
from sys import maxsize  
  
# defining a constant value for the number of nodes  
V = 4  
  
# defining the method to find the minimum weight Hamiltonian Cycle  
def travelling_salesman_problem(graph, n):  
      
    # creating an empty list to store the number of numbers  
    nodes = []  
      
    # iterating through the number of nodes and adding elements into the array if the current value is not equal to source node  
    for i in range(V):  
        if i != n:  
            nodes.append(i)  
  
    # setting an initial value for minimum path as Integer's maximum value  
    minimumPath = maxsize  
      
    # instantiating the permutations() class  
    nextPermutation = permutations(nodes)  
      
    # iterating through each permutation and updating the minimum path weight  
    for i in nextPermutation:  
          
        # initializing the current path weight as 0  
        currentPathWeight = 0  
        k = n  
          
        # iterating through the list and incrementing the current path weight  
        for j in i:  
            currentPathWeight += graph[k][j]  
            k = j  
        currentPathWeight += graph[k][n]  
          
        # updating the minimum path weight  
        minimumPath = min(minimumPath, currentPathWeight)  
          
    return minimumPath  
  
# main function  
if __name__ == "__main__":  
      
    # defining the nodes of the graph  
    graph = [  
        [ 0, 12, 18, 24 ],  
        [ 12, 0, 36, 28 ],  
        [ 18, 36, 0, 32 ],  
        [ 24, 28, 32, 0 ]  
    ]  
      
    # starting node  
    n = 0  
      
    # calling the travelling_salesman_problem() function  
    minimumPathWeight = travelling_salesman_problem(graph, n)  
      
    # printing the result for the users  
    print("Minimum Cost :", minimumPathWeight)  