import math
import random
import time
import csv
import heapq

# --- Helper Functions ---
def euclidean_distance(a, b):
    """Compute Euclidean distance between two points.
       Assumes a and b are tuples where the first two elements are X and Y coordinates."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def total_distance(route, cities):
    """Calculate the total travel distance for a given route of cities."""
    dist = 0
    n = len(route)
    for i in range(n):
        # Compute distance between consecutive cities, wrapping around to the start
        dist += euclidean_distance(cities[route[i - 1]], cities[route[i]])
    return dist

def load_cities_from_csv(filename):
    """
    Load cities from a CSV file.
    Assumes CSV rows in the format: X, Y, City_Name
    Returns:
      - cities: list of (X, Y) tuples for distance computations
      - city_names: list of city names corresponding to each city
    """
    cities = []
    city_names = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x = float(row['X'])
            y = float(row['Y'])
            name = row['City_Name']
            cities.append((x, y))
            city_names.append(name)
    return cities, city_names


# --- Heuristic Helpers ---
def mst_cost(nodes, dist):
    """
    Compute the cost of a Minimum Spanning Tree (MST) for the given nodes using Prim's algorithm.
    """
    if not nodes:
        return 0
    nodes = list(nodes)
    cost = 0
    visited = {nodes[0]}
    remaining = set(nodes[1:])
    while remaining:
        min_edge = math.inf
        min_node = None
        for u in visited:
            for v in remaining:
                if dist[u][v] < min_edge:
                    min_edge = dist[u][v]
                    min_node = v
        cost += min_edge
        visited.add(min_node)
        remaining.remove(min_node)
    return cost

def heuristic(current, visited, n, dist):
    """
    Heuristic for A* search:
    - Compute MST cost for all unvisited nodes.
    - Add the minimum edge from the current city to any unvisited city.
    - Add the minimum edge from any unvisited city back to the start.
    """
    remaining = set(range(n)) - visited
    if not remaining:
        return dist[current][0]  # Only the cost to return to start remains.
    mst = mst_cost(remaining, dist)
    min_from_current = min(dist[current][j] for j in remaining)
    min_to_start = min(dist[j][0] for j in remaining)
    return mst + min_from_current + min_to_start

# -- Custom Dataset --

def get_custom_data():
    """
    Prompt the user to input custom city data.
    Returns a tuple: (list of (x, y) coordinate tuples, list of city names)
    """
    cities = []
    city_names = []
    print("Enter custom city data. Type 'done' as the city name to finish.")
    
    while True:
        # Display a running tracker of how many cities have been entered
        print(f"Cities entered so far: {len(cities)}")
        name = input("City name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        try:
            x = float(input("Enter x coordinate: ").strip())
            y = float(input("Enter y coordinate: ").strip())
        except ValueError:
            print("Coordinates must be numbers. Please try again.")
            continue
        cities.append((x, y))
        city_names.append(name)
        print(f"City '{name}' added successfully!\n")
    
    print(f"Finished entering data. Total cities entered: {len(cities)}")
    return cities, city_names
