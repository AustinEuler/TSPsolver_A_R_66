from utils import math, random, time, csv, heapq, total_distance

# --- Algorithm 1: Hill Climbing ---
def hill_climbing_tsp(cities):
    """
    Hill Climbing for TSP.
    Iteratively swap two cities and accept the swap only if it reduces the total distance.
    """
    n = len(cities)
    # Start with a random route
    current_route = list(range(n))
    random.shuffle(current_route)
    best_distance = total_distance(current_route, cities)
    improvement = True
    iterations = 0
    start_time = time.time()

    while improvement:
        improvement = False
        for i in range(n - 1):
            for j in range(i + 1, n):
                new_route = current_route.copy()
                # Swap two cities
                new_route[i], new_route[j] = new_route[j], new_route[i]
                new_distance = total_distance(new_route, cities)
                iterations += 1
                if new_distance < best_distance:
                    current_route = new_route
                    best_distance = new_distance
                    improvement = True
                    break  # Accept first improvement found
            if improvement:
                break  # Restart search after an improvement
    execution_time = time.time() - start_time
    return current_route, best_distance, execution_time, iterations