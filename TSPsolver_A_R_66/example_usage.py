from tests import test_random_search, test_Asearch, test_simulated_annealing, test_hill_climbing

def main():
    menu_options = {
        '1': ('Random Search', test_random_search.main),
        '2': ('A* Search', test_Asearch.main),
        '3': ('Simulated Annealing', test_simulated_annealing.main),
        '4': ('Hill Climbing', test_hill_climbing.main),
        '5': ('Exit', None)
    }
    
    while True:
        print("\n=== Algorithm Test Menu ===")
        for key, (name, _) in menu_options.items():
            print(f"{key}. {name}")
            
        choice = input("Enter the number of the algorithm to test: ").strip()
        
        if choice not in menu_options:
            print("Invalid choice. Please try again.")
            continue
        
        if choice == '5':
            print("Exiting the test hub.")
            break
        
        test_name, test_function = menu_options[choice]
        print(f"\nStarting {test_name} test...\n")
        test_function()  # Call the selected test's main() function

if __name__ == '__main__':
    main()