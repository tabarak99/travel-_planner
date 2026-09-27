
import time

travel_data = {
    "paris": {
        "country": "France",
        "currency": "Euro",
        "language": "French",
        "best_time": "April to June",
        "attractions": ["Eiffel Tower", "Louvre Museum", "Notre-Dame"],
        "daily_budget": "$150 - $250"
    },
    "baghdad": {
        "country": "Iraq",
        "currency": "Iraqi Dinar",
        "language": "Arabic",
        "best_time": "November to March",
        "attractions": ["National Museum", "Ziggurat of Ur", "Mutannabi Street"],
        "daily_budget": "$50 - $100"
    },
    "tokyo": {
        "country": "Japan",
        "currency": "Japanese Yen",
        "language": "Japanese",
        "best_time": "March to May",
        "attractions": ["Shibuya Crossing", "Senso-ji Temple", "Tokyo Tower"],
        "daily_budget": "$120 - $200"
    }
}

def show_plan(destination, days, budget_level):
    info = travel_data[destination]
    print("\n" + "="*50)
    print(f"TRAVEL PLAN FOR: {destination.upper()}")
    print("="*50)
    print(f"Country       : {info['country']}")
    print(f"Currency      : {info['currency']}")
    print(f"Language      : {info['language']}")
    print(f"Best Time     : {info['best_time']}")
    print(f"Daily Budget  : {info['daily_budget']}")
    print("-" * 50)
    print(f"Trip Duration : {days} days")
    print(f"Budget Level  : {budget_level}")
    print("-" * 50)
    print("Top Attractions:")
    for i, place in enumerate(info["attractions"], 1):
        print(f"   {i}. {place}")
    
    if budget_level.lower() == "low":
        cost_per_day = 60
    elif budget_level.lower() == "medium":
        cost_per_day = 150
    else:
        cost_per_day = 300
    
    total_cost = cost_per_day * days
    print("-" * 50)
    print(f"Estimated Total Cost: ${total_cost} (approx.)")
    print("="*50)
    print("Have a wonderful trip!")
    print("="*50 + "\n")

def main():
    print("\n" + "="*50)
    print("WELCOME TO THE TRAVEL PLANNER!")
    print("="*50)
    print("Available destinations: paris, baghdad, tokyo")
    
    while True:
        destination = input("\nEnter destination (or 'exit' to quit): ").strip().lower()
        
        if destination == 'exit':
            print("Goodbye!")
            break
        
        if destination not in travel_data:
            print(f"Sorry, '{destination}' is not in our database.")
            continue
        
        try:
            days = int(input("Enter number of days: ").strip())
            if days <= 0:
                print("Number of days must be positive.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        budget_level = input("Enter budget level (Low / Medium / High): ").strip()
        show_plan(destination, days, budget_level)

if __name__ == "__main__":
    main()
