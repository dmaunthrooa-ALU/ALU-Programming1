# car.py
# This file contains only the Car class

class Car:
    """Represents one car in Omondi's rental fleet."""

    def __init__(self, plate, model, year_released, year_acquired):
        self.plate = plate
        self.model = model
        self.year_released = year_released
        self.year_acquired = year_acquired
        self.money_made = 0
        self.times_rented = 0

    def rent(self, amount):
        """Record a rental: add money and increase rental count."""
        if amount <= 0:
            print("Rental amount must be positive.")
            return
        self.times_rented += 1
        self.money_made += amount
        print(f"{self.plate} rented. Total rentals: {self.times_rented}, Money: {self.money_made}")

    def get_info(self):
        """Return a short description of the car."""
        return (f"{self.plate} | {self.model} | "
                f"Released {self.year_released} | Acquired {self.year_acquired} | "
                f"Rented {self.times_rented} times | Earned {self.money_made} KES")
