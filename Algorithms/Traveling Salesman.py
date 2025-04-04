distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
from itertools import permutations
def tsp_brute_force(distance):
    #if not given, first we should get number of cities
    cities = list(range(len(distance)))
    #lets set the starting point
    start = cities[0]
    min_path = None #set min path to none because at this point we dont have any
    min_cost = float('inf') #set the min_cost to highest
    for perm in permutations(cities[1:]): #permutations is a function to generate permutation of given list like [1,2,3], [1,3,2] soon
        current_path  = [start]+list(perm) # current path will be as [0] + [1,2,3] => [0,1,2,3] or [0] + [1,3,2]
        current_cost = 0
        for i in range(len(current_path)-1): #iterates over current_path
            current_cost += distance[current_path[i]][current_path[i+1]]
        current_cost += distance[current_path[-1]][start]
        if current_cost<min_cost:
            min_cost = current_cost
            min_path = current_path
    return min_path, min_cost

best_path, best_cost = tsp_brute_force(distance)
print("Best Route:", best_path + [best_path[0]])  # to show full cycle
print("Minimum Cost:", best_cost)

