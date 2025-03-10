from  utils import load_cities_from_csv, get_custom_data
from  algorithms.simulated_annealing import simulated_annealing_tsp


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

    # Run Simulated Annealing
    if not custom:
        print("Running Simulated Annealing on first 100 cities of provided dataset...")
    else:
        print(f"Running Simulated Annealing on custom dataset of {len(cities)} cities...")

    route_sa, distance_sa, time_sa, iter_sa = simulated_annealing_tsp(cities)
    print("Simulated Annealing Results:")
    print("  Best Route (indices):", route_sa)
    print("  Best Route (city names):", [city_names[i] for i in route_sa])
    print()
    print("  Total Distance:", distance_sa)
    print("  Execution Time: {:.2f} sec".format(time_sa))
    print("  Iterations:", iter_sa)
    print()


if __name__ == '__main__':
    main()