# ==========================================================
# OMONDI'S CAR RENTAL BUSINESS – using Dictionaries
# ==========================================================

# Starting fleet of 5 cars
# Key = plate number (unique identifier)
# Value = dictionary with all details of that car
fleet = {
    "KAA 123A": {
        "model": "Toyota Corolla",
        "year_released": 2018,
        "year_acquired": 2022,
        "money_made": 0,
        "times_rented": 0
    },
    "KBB 456B": {
        "model": "Honda Fit",
        "year_released": 2019,
        "year_acquired": 2023,
        "money_made": 0,
        "times_rented": 0
    },
    "KCC 789C": {
        "model": "Mazda Demio",
        "year_released": 2017,
        "year_acquired": 2021,
        "money_made": 0,
        "times_rented": 0
    },
    "KDD 101D": {
        "model": "Nissan Note",
        "year_released": 2020,
        "year_acquired": 2023,
        "money_made": 0,
        "times_rented": 0
    },
    "KEE 202E": {
        "model": "Suzuki Swift",
        "year_released": 2016,
        "year_acquired": 2020,
        "money_made": 0,
        "times_rented": 0
    }
}


# ----------------------------------------------------------
# FUNCTION 1: Show all cars
# ----------------------------------------------------------
def show_fleet():
    """Print every car currently in the fleet with its details."""
    print("\n========== CURRENT FLEET ==========")
    if len(fleet) == 0:
        print("No cars in the fleet.")
        return
    # Loop through both plate (key) and details (value)
    for plate, details in fleet.items():
        print(f"Plate: {plate}")
        print(f"  Model          : {details['model']}")
        print(f"  Year released  : {details['year_released']}")
        print(f"  Year acquired  : {details['year_acquired']}")
        print(f"  Money made     : {details['money_made']} KES")
        print(f"  Times rented   : {details['times_rented']}")
        print("-" * 35)


# ----------------------------------------------------------
# FUNCTION 2: Rent a car
# ----------------------------------------------------------
def rent_car(plate, amount):
    """Rent a car: increase times_rented and add money made."""
    # First check that the car actually exists
    if plate not in fleet:
        print(f"Sorry, no car with plate {plate} found.")
        return

    # Update the two values
    fleet[plate]["times_rented"] += 1
    fleet[plate]["money_made"] += amount

    print(f"Car {plate} rented successfully!")
    print(f"  New times rented : {fleet[plate]['times_rented']}")
    print(f"  New money made   : {fleet[plate]['money_made']} KES")


# ----------------------------------------------------------
# FUNCTION 3: Add a new car
# ----------------------------------------------------------
def add_car(plate, model, year_released, year_acquired):
    """Add a brand-new car to the fleet. Starts with 0 money and 0 rentals."""
    # Prevent duplicate plate numbers
    if plate in fleet:
        print(f"A car with plate {plate} already exists.")
        return

    # Create the new car dictionary and insert it
    fleet[plate] = {
        "model": model,
        "year_released": year_released,
        "year_acquired": year_acquired,
        "money_made": 0,
        "times_rented": 0
    }
    print(f"Car {plate} ({model}) added successfully!")


# ----------------------------------------------------------
# FUNCTION 4: Remove a car
# ----------------------------------------------------------
def remove_car(plate):
    """Remove a car from the fleet using its plate number."""
    if plate not in fleet:
        print(f"No car with plate {plate} found.")
        return

    # pop() removes the key and returns its value
    removed = fleet.pop(plate)
    print(f"Car {plate} ({removed['model']}) has been removed.")


# ----------------------------------------------------------
# FUNCTION 5: Show rental statistics
# ----------------------------------------------------------
def show_stats():
    """Show how many times each car was rented and money made."""
    print("\n========== RENTAL STATISTICS ==========")
    total_money = 0
    total_rentals = 0

    for plate, details in fleet.items():
        print(f"{plate} – {details['model']}")
        print(f"  Times rented : {details['times_rented']}")
        print(f"  Money made   : {details['money_made']} KES")
        total_money += details["money_made"]
        total_rentals += details["times_rented"]
        print()

    print(f"TOTAL RENTALS : {total_rentals}")
    print(f"TOTAL MONEY   : {total_money} KES")


# ----------------------------------------------------------
# MAIN PROGRAM – simple interactive menu
# ----------------------------------------------------------
def main():
    """Simple text menu so Omondi can manage his business."""
    while True:
        print("\n===== OMONDI CAR RENTAL =====")
        print("1. Show all cars")
        print("2. Rent a car")
        print("3. Add a new car")
        print("4. Remove a car")
        print("5. Show rental statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            show_fleet()

        elif choice == "2":
            plate = input("Enter plate number: ").upper()
            amount = int(input("Enter rental amount (KES): "))
            rent_car(plate, amount)

        elif choice == "3":
            plate = input("New plate number: ").upper()
            model = input("Model: ")
            year_rel = int(input("Year released: "))
            year_acq = int(input("Year acquired: "))
            add_car(plate, model, year_rel, year_acq)

        elif choice == "4":
            plate = input("Plate number to remove: ").upper()
            remove_car(plate)

        elif choice == "5":
            show_stats()

        elif choice == "6":
            print("Thank you! Goodbye.")
            break

        else:
            print("Invalid choice. Please enter 1-6.")


# Start the program only when this file is run directly
if __name__ == "__main__":
    main()
