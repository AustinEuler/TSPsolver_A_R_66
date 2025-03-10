from utils import random, time, csv, total_distance

def random_search_tsp(cities, iterations=10000):
    """
    Random Search for TSP.
    Generates a random tour in each iteration and keeps track of the best tour found.
    
    Parameters:
      - cities: list of city coordinates (X, Y)
      - iterations: number of random tours to generate
      
    Returns:
      - best_route: the best route found (list of city indices)
      - best_distance: total distance of the best route
      - execution_time: time taken to perform the search
      - iterations: the total number of iterations performed
    """
    n = len(cities)
    best_route = None
    best_distance = float('inf')
    start_time = time.time()
    
    for i in range(iterations):
        route = list(range(n))
        random.shuffle(route)
        current_distance = total_distance(route, cities)
        if current_distance < best_distance:
            best_distance = current_distance
            best_route = route[:]
    
    execution_time = time.time() - start_time
    return best_route, best_distance, execution_time, iterations
