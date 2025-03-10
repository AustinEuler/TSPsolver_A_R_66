from  utils import load_cities_from_csv, get_custom_data
from  algorithms.hill_climbing import hill_climbing_tsp

def main():
    custom = False
    use_provided = input("Do you want to use the provided dataset? (y/n): ").strip().lower()
    if use_provided in ['y', 'yes']:
        filename = 'TSP_Large_Dataset__500_Cities__-_Primary.csv'
        cities, city_names = load_cities_from_csv(filename)
        # Only track the first 100 cities to speed up computations
        cities = cities[:100]
        city_names = city_names[:100]
    else:
        custom = True
        print("Please input your custom data:")
        cities, city_names = get_custom_data()


    # Run Hill Climbing
    if not custom:
        print("Running Hill Climbing on first 100 cities of provided dataset...")
    else:
        print(f"Running Hill Climbing on custom dataset of {len(cities)} cities...")

    route_hc, distance_hc, time_hc, iter_hc = hill_climbing_tsp(cities)
    print("Hill Climbing Results:")
    print("  Best Route (indices):", route_hc)
    print("  Best Route (city names):", [city_names[i] for i in route_hc])
    print()
    print("  Total Distance:", distance_hc)
    print("  Execution Time: {:.2f} sec".format(time_hc))
    print("  Iterations:", iter_hc)
    print()

if __name__ == '__main__':
    main()