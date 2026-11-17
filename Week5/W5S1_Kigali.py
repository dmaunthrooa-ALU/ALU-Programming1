# ==========================================================
# elevator.py  –  Kigali Heights Elevator System
# ==========================================================

class Elevator:
    """Simulates one elevator in a building."""

    def __init__(self, total_floors=10, start_floor=0):
        # total_floors – how many floors the building has
        # start_floor  – where the elevator is when the program starts
        self.total_floors = total_floors
        self.current_floor = start_floor
        self.is_open = False  # doors start closed
        self.direction = "idle"  # "up", "down" or "idle"

    def status(self):
        """Tell the user the current state of the elevator."""
        door = "OPEN" if self.is_open else "CLOSED"
        print(f"Elevator is on floor {self.current_floor} | Doors: {door} | Direction: {self.direction}")

    def open_door(self):
        """Open the elevator doors."""
        if self.is_open:
            print("Doors are already open.")
            return
        self.is_open = True
        print("Doors opening...")

    def close_door(self):
        """Close the elevator doors."""
        if not self.is_open:
            print("Doors are already closed.")
            return
        self.is_open = False
        print("Doors closing...")

    def move_to(self, target_floor):
        """Move the elevator to the requested floor."""
        if target_floor < 0 or target_floor > self.total_floors:
            print(f"Invalid floor. Building has floors 0 to {self.total_floors}.")
            return
        if target_floor == self.current_floor:
            print("You are already on that floor.")
            return
        if self.is_open:
            print("Please close the doors before moving.")
            return

        # Decide direction
        if target_floor > self.current_floor:
            self.direction = "up"
        else:
            self.direction = "down"

        print(f"Moving {self.direction} from floor {self.current_floor} to floor {target_floor}...")

        # Simulate the movement floor by floor so the user sees progress
        step = 1 if self.direction == "up" else -1
        while self.current_floor != target_floor:
            self.current_floor += step
            print(f"  ... now at floor {self.current_floor}")

        self.direction = "idle"
        print(f"Arrived at floor {self.current_floor}.")
        self.open_door()  # automatically open doors on arrival


# ===== Main program =====
def main():
    lift = Elevator(total_floors=10, start_floor=0)

    print("=== Kigali Heights Elevator ===")
    lift.status()

    while True:
        print("\nOptions:")
        print("1. Open doors")
        print("2. Close doors")
        print("3. Go to a floor")
        print("4. Show status")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            lift.open_door()
        elif choice == "2":
            lift.close_door()
        elif choice == "3":
            floor = int(input("Which floor? "))
            lift.move_to(floor)
        elif choice == "4":
            lift.status()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
