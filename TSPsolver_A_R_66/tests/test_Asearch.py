from  utils import load_cities_from_csv, get_custom_data
from  algorithms.Asearch import a_star_tsp



def main():
    custom = False
    use_provided = input("Do you want to use the provided dataset? (y/n): ").strip().lower()
    if use_provided in ['y', 'yes']:
        filename = 'TSP_Large_Dataset__500_Cities__-_Primary.csv'
        cities, city_names = load_cities_from_csv(filename)
        # Only track the first 25 cities to speed up computations
        cities = cities[:25]
        city_names = city_names[:25]
    else:
        custom = True
        print("DISCLAIMER: Please keep city count <= 25 for speed purposes!")
        print("Please input your custom data:")
        cities, city_names = get_custom_data()
    
    if not custom:
        print("\nRunning A* Search on first 25 cities...")
    else:
        print(f"Running Hill Climbing on custom dataset of {len(cities)} cities...")

    route_astar, distance_astar, time_astar, iter_astar = a_star_tsp(cities)
    print("A* Search Results:")
    print("  Best Route (indices):", route_astar)
    print("  Best Route (city names):", [city_names[i] for i in route_astar])
    print()
    print("  Total Distance:", distance_astar)
    print("  Execution Time: {:.2f} sec".format(time_astar))
    print("  Iterations:", iter_astar)
    print()

if __name__ == '__main__':
    main()