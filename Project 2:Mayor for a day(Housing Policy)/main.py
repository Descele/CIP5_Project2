
"""
Hello World!Desiree Cele built this Housing Policy Game to show how coding can help solve real city problems. 
Using simple Python(using only random and simple Input/Output), the program lets you play as a Mayor choosing policies 
to make homes more affordable - with each decision changing the results. As you play, you'll learn how basic programming can create useful tools for understanding housing challenges.
NB. This program demonstrates how even basic Python skills can automate housing market analysis,model policy outcomes,
generate data-driven recommendations and visualize complex trends in a simple way.
"""
import random

def print_section(title):
    """Prints a decorated section header"""
    print(f"\n{'='*40}")
    print(f"|| {title.upper():^34} ||")
    print(f"{'='*40}")

def print_divider():
    """Prints a visual separator"""
    print(f"\n{'*'*40}\n")

def main():
    print("\n" + "🏘️"*5 + " HOUSING POLICY GAME " + "🏘️"*5)
    print("\nHelp your city solve its housing crisis!\n")
    
    # City data
    city = {
        "name": "Tinyville",
        "budget": 100000,
        "homes": random.randint(1000, 5000),
        "homeless": random.randint(50, 500),
        "price": random.randint(150000, 750000),
        "salary": random.randint(30000, 70000)
    }
    
    # ===== CITY STATUS SECTION =====
    print_section("City Status")
    print(f"\nWelcome, Mayor of {city['name']}!")
    print(f"💰 Your Budget is: ${city['budget']:,}")
    
    print("\n" + "-"*30)
    print("🏠 DEAL WITH CURRENT HOUSING CRISIS:")
    print(f" Homes Available: {city['homes']:,}")
    print(f" Homeless Population: {city['homeless']:,}")
    print(f" Average Home Price: ${city['price']:,}")
    print(f" Teacher Salary: ${city['salary']:,}/yr")
    
    ratio = round(city['price'] / max(city['salary'], 1), 1)
    print(f"\n📊 AFFORDABILITY: {ratio}x salary needed to buy a home")
    
    # ===== POLICY SELECTION =====
    print_section("Policy Options")
    print("\nChoose 2 policies to prioritise BELOW (${:,} each):".format(city['budget']//2))
  
    policies = [
        "1. 🏗️ Build affordable housing (+50-150 homes)",
        "2. 💵 Rent stabilization (-5-15% prices)",
        "3. 🚍 Upgrade public transit (+20-80 homes, -10-20% prices)",
        "4. 🏚️ Tax vacant properties (+100-300 homes)"
    ]
    
    print_divider()
    for policy in policies:
        print(f"| {policy}")
    print_divider()
    
    # Get policy choices
    choices = []
    while len(choices) < 2:
        try:
            choice = int(input(f"Choice {len(choices)+1} (1-4): "))
            if 1 <= choice <= 4:
                if choice not in choices:
                    choices.append(choice)
                else:
                    print("|> You already chose that policy! Pick another.")
            else:
                print("|> Please enter 1-4")
        except ValueError:
            print("|> Please enter a number")
    print("Waiting for policy outcomes...⏳")
    
    # ===== POLICY RESULTS =====
    print_section("Policy Outcomes")
    original_homes = city['homes']
    original_price = city['price']
    
    for choice in choices:
        print("\n" + "-"*30)
        if choice == 1:
            added = random.randint(50, 150)
            city['homes'] += added
            print(f"🏗️ You built {added} affordable homes!")
        elif choice == 2:
            reduction = random.randint(5, 15)
            city['price'] = max(int(city['price'] * (1 - reduction/100)), 100000)
            print(f"💵 Home prices dropped by {reduction}%!")
        elif choice == 3:
            added = random.randint(20, 80)
            reduction = random.randint(10, 20)
            city['homes'] += added
            city['price'] = max(int(city['price'] * (1 - reduction/100)), 100000)
            print(f"🚍 Added {added} homes near transit!")
            print(f"   Home prices reduced by {reduction}%!")
        elif choice == 4:
            added = random.randint(100, 300)
            city['homes'] += added
            print(f"🏚️ You freed up {added} vacant properties!")
    
    # ===== FINAL RESULTS =====
    print_section("Final Report")
    new_ratio = round(city['price'] / max(city['salary'], 1), 1)
    
    print("\n📊 BEFORE vs AFTER:")
    print(f"| {'Homes:':<15} | {original_homes:>8,} → {city['homes']:>8,} (+{city['homes']-original_homes})")
    print(f"| {'Home Price:':<15} | ${original_price:>7,} → ${city['price']:>7,}")
    print(f"| {'Affordability:':<15} | {ratio:>8}x → {new_ratio:>8}x salary")
    print("\n" + "★"*45)
    
    if new_ratio < ratio:
        print("🎉 SUCCESS! You made housing more affordable!")
    elif new_ratio == ratio and city['homes'] > original_homes:
        print("👍 Progress! More homes added but same affordability")
    else:
        print("😬 Prices still too high. Try different policies!")
    print("★"*45)




if __name__ == "__main__":
    main()