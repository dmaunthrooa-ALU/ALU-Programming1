class StringProcessor:
    """A simple class that gets a string and prints it in uppercase."""

    def __init__(self):
        # Start with an empty string
        self.text = ""

    def get_String(self):
        # Ask the user for a string and store it
        self.text = input("Enter a string: ")

    def print_String(self):
        # Print the stored string in UPPERCASE
        print(self.text.upper())


# ===== Example usage =====
sp = StringProcessor()
sp.get_String()  # user types something
sp.print_String()  # prints it in capital letters
