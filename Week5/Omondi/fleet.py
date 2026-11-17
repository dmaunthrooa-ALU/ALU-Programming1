# fleet.py
# This file manages the collection of Car objects

from car import Car  # import the Car class from the other file

# The fleet is a dictionary: key = plate, value = Car object
fleet = {}


def add_car(plate, model, year_released, year_acquired):
    """Create a Car and add it to the fleet."""
    if plate in fleet:
        print("Plate already exists.")
        return
    new_car = Car(plate, model, year_released, year_acquired)
    fleet[plate] = new_car
    print(f"Added {plate}")


def remove_car(plate):
    """Remove a car from the fleet."""
    if plate not in fleet:
        print("Car not found.")
        return
    removed = fleet.pop(plate)
    print(f"Removed {removed.plate} ({removed.model})")


def rent_car(plate, amount):
    """Rent a specific car."""
    car = fleet.get(plate)
    if car is None:
        print("Car not found.")
        return
    car.rent(amount)


def show_fleet():
    """Print every car."""
    if not fleet:
        print("Fleet is empty.")
        return
    for car in fleet.values():
        print(car.get_info())


def show_stats():
    """Show total money and total rentals."""
    total_money = sum(c.money_made for c in fleet.values())
    total_rentals = sum(c.times_rented for c in fleet.values())
    print(f"Total rentals: {total_rentals}")
    print(f"Total money  : {total_money} KES")
