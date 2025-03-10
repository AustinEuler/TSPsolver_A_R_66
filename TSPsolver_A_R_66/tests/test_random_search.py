from  utils import load_cities_from_csv, get_custom_data
from  algorithms.random_search import random_search_tsp

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


    # Run Random Search
    if not custom:
        print("Running Random Search on first 100 cities of provided dataset...")
    else:
        print(f"Running Random Search on custom dataset of {len(cities)} cities...")

    route_rs, distance_rs, time_rs, iter_rs = random_search_tsp(cities, iterations=10000)

    print("Random Search Results:")
    print("  Best Route (indices):", route_rs)
    print("  Best Route (city names):", [city_names[i] for i in route_rs])
    print()
    print("  Total Distance:", distance_rs)
    print("  Execution Time: {:.2f} sec".format(time_rs))
    print("  Iterations:", iter_rs)
    print()

if __name__ == '__main__':
    main()