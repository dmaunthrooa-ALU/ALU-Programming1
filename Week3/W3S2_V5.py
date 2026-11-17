import sys
import subprocess

def ensure_dateutil():
    """Check if python-dateutil is installed. If not, install it."""
    try:
        import dateutil  # noqa: F401
        print("python-dateutil is already installed.")
    except ImportError:
        print("python-dateutil not found. Installing it now...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "python-dateutil"],
                stdout=subprocess.DEVNULL,   # hide pip output (optional)
                stderr=subprocess.STDOUT
            )
            print("python-dateutil installed successfully.\n")
        except subprocess.CalledProcessError:
            print("Failed to install python-dateutil. Please install it manually:")
            print("    pip install python-dateutil")
            sys.exit(1)

# Make sure the library is available before we import it
ensure_dateutil()

# Now it is safe to import
from datetime import datetime
from dateutil import parser
from dateutil.parser import ParserError


def parse_date(user_input):
    text = user_input.strip()
    try:
        # dayfirst=True prefers DD/MM over MM/DD
        return parser.parse(text, dayfirst=True)
    except (ParserError, ValueError):
        return None


def get_day_of_week(day_of_birth):
    return day_of_birth.strftime("%A")


def get_ashanti_name(day_of_week, gender):
    female_names = {
        "Sunday": "Akosua",
        "Monday": "Adwoa",
        "Tuesday": "Abeena",
        "Wednesday": "Akwa",
        "Thursday": "Yaa",
        "Friday": "Afia",
        "Saturday": "Amma"
    }

    male_names = {
        "Sunday": "Kwasi",
        "Monday": "Kadjo",
        "Tuesday": "Kwabena",
        "Wednesday": "Kwaku",
        "Thursday": "Yaw",
        "Friday": "Kofi",
        "Saturday": "Kwame"
    }

    gender = gender.strip().lower()

    if gender in ("female", "f", "girl", "woman"):
        return female_names.get(day_of_week, "Unknown")
    elif gender in ("male", "m", "boy", "man"):
        return male_names.get(day_of_week, "Unknown")
    else:
        return "Unknown"


def main():
    print("Ashanti Name Finder\n")

    date_of_birth = None
    while date_of_birth is None:
        dob_input = input("Enter your date of birth: ")
        date_of_birth = parse_date(dob_input)
        if date_of_birth is None:
            print("Please enter a valid date of birth.\n")

    gender = input("Enter your gender (Male / Female): ")
    day = get_day_of_week(date_of_birth)
    name = get_ashanti_name(day, gender)

    print("\nYou were born on a " + day + ".")
    print("Your Ashanti name could have been: " + name)


if __name__ == "__main__":
    main()