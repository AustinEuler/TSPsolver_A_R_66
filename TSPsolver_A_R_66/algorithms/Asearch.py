from utils import math, time, csv, heapq, euclidean_distance, heuristic


# --- A* Search for TSP ---
def a_star_tsp(cities):
    """
    A* search for the Traveling Salesman Problem.
    Returns:
      - best complete route (list of city indices)
      - total distance of that route
      - execution time (in seconds)
      - number of iterations (state expansions)
    """
    n = len(cities)
    # Precompute distance matrix.
    dist = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # Each state: (f, g, current, visited, path)
    # f = g + h, where g is the cost so far, and h is the heuristic.
    start_state = (heuristic(0, frozenset({0}), n, dist), 0, 0, frozenset({0}), [0])
    heap = [start_state]
    iterations = 0
    start_time = time.time()
    
    while heap:
        f, g, current, visited, path = heapq.heappop(heap)
        iterations += 1
        
        # Check if a complete tour has been formed.
        if len(visited) == n:
            total_cost = g + dist[current][0]  # add cost to return to starting city.
            return path + [0], total_cost, time.time() - start_time, iterations
        
        # Expand the current state: try visiting each unvisited city.
        for next_city in range(n):
            if next_city not in visited:
                new_g = g + dist[current][next_city]
                new_visited = visited | {next_city}
                new_path = path + [next_city]
                h = heuristic(next_city, new_visited, n, dist)
                new_f = new_g + h
                heapq.heappush(heap, (new_f, new_g, next_city, new_visited, new_path))
    
    # If no complete route is found (should not happen for connected graphs).
    return None, math.inf, time.time() - start_time, iterations
