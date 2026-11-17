class Rectangle:
    """Represents a rectangle and can calculate its area."""

    def __init__(self, length, width):
        # Store the dimensions when the object is created
        self.length = length
        self.width = width

    def area(self):
        # Return length × width
        return self.length * self.width


# ===== Example usage =====
rect = Rectangle(10, 5)
print("Area:", rect.area())  # 50
