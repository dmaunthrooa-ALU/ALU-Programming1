# main.py
# This is the only file you run. It imports the other modules.

import fleet  # import the whole fleet module


def main():
    # Start with a few cars
    fleet.add_car("KAA 123A", "Toyota Corolla", 2018, 2022)
    fleet.add_car("KBB 456B", "Honda Fit", 2019, 2023)
    fleet.add_car("KCC 789C", "Mazda Demio", 2017, 2021)

    while True:
        print("\n===== OMONDI CAR RENTAL =====")
        print("1. Show fleet")
        print("2. Rent a car")
        print("3. Add a car")
        print("4. Remove a car")
        print("5. Show statistics")
        print("6. Exit")

        choice = input("Choice (1-6): ")

        if choice == "1":
            fleet.show_fleet()
        elif choice == "2":
            plate = input("Plate: ").upper()
            amount = int(input("Amount (KES): "))
            fleet.rent_car(plate, amount)
        elif choice == "3":
            plate = input("Plate: ").upper()
            model = input("Model: ")
            yr = int(input("Year released: "))
            ya = int(input("Year acquired: "))
            fleet.add_car(plate, model, yr, ya)
        elif choice == "4":
            plate = input("Plate to remove: ").upper()
            fleet.remove_car(plate)
        elif choice == "5":
            fleet.show_stats()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
