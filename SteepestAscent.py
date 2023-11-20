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

def getNeighbours(solution):
      neighbours = []
      for i in range(len(solution)):
          for j in range(i + 1, len(solution)):
              neighbour = solution.copy()
              neighbour[i] = solution[j]
              neighbour[j] = solution[i]
              neighbours.append(neighbour)
      return neighbours

def getBestNeighbour(tsp, neighbours):
    bestRouteLength = routeLength(tsp, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength

def hillClimbing(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)
    i = 0
    while bestNeighbourRouteLength < currentRouteLength:
        print(currentSolution,'->',end=' ')
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)
    print(currentSolution)
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