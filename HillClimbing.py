import random

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    random.shuffle(cities)
    return cities

def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength


def hillClimbing(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currentSolution)
    print('Initial solution: ', (currentSolution,currentRouteLength))
    i = 0 
    flag = False
    while i < len(currentSolution):
        for j in range(i + 1, len(currentSolution)):
            neighbour = currentSolution.copy()
            neighbour[i] = currentSolution[j]
            neighbour[j] = currentSolution[i]
            if routeLength(tsp, neighbour) < currentRouteLength:
                currentSolution = neighbour
                currentRouteLength = routeLength(tsp, neighbour)
                flag = True
                break
        if flag:
            flag = False
            i = 0
        else:
            i += 1
    
    return currentSolution, currentRouteLength


def main():
    tsp = [[0, 10, 15, 20], 
           [10, 0, 35, 25], 
           [15, 35, 0, 30],
           [20, 25, 30, 0]
           ]


    print("Final Solution: ", hillClimbing(tsp))

if __name__ == "__main__":
    main()
