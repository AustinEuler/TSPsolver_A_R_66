from utils import math, time, random, total_distance

# --- Algorithm 2: Simulated Annealing ---
def simulated_annealing_tsp(cities, initial_temp=10000, cooling_rate=0.995, iterations=10000):
    """
    Simulated Annealing for TSP.
    Starts with a random route and a high temperature to allow non-improving moves,
    then gradually cools down.
    """
    n = len(cities)
    current_route = list(range(n))
    random.shuffle(current_route)
    current_distance = total_distance(current_route, cities)
    best_route = current_route[:]
    best_distance = current_distance
    T = initial_temp
    iter_count = 0
    start_time = time.time()

    for i in range(iterations):
        # Randomly swap two cities to generate a neighbor
        a, b = random.sample(range(n), 2)
        new_route = current_route[:]
        new_route[a], new_route[b] = new_route[b], new_route[a]
        new_distance = total_distance(new_route, cities)
        iter_count += 1

        # Decide whether to accept the new route
        if new_distance < current_distance or random.random() < math.exp(-(new_distance - current_distance) / T):
            current_route = new_route
            current_distance = new_distance

        # Update the best found route
        if current_distance < best_distance:
            best_route = current_route[:]
            best_distance = current_distance

        # Cool down
        T *= cooling_rate

    execution_time = time.time() - start_time
    return best_route, best_distance, execution_time, iter_count
