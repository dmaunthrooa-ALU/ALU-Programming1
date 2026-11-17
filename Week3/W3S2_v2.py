# Import the datetime class so we can work with real dates
from datetime import datetime


def get_ashanti_name(day_of_week, gender):
    #Return the Ashanti day name using two lookup tables

    # Dictionary that maps each weekday to its female name
    # The key is the day, the value is the name
    female_names = {
        "Sunday": "Akosua",
        "Monday": "Adwoa",
        "Tuesday": "Abeena",
        "Wednesday": "Akwa",
        "Thursday": "Yaa",
        "Friday": "Afia",
        "Saturday": "Amma"
    }

    # Dictionary that maps each weekday to its male name
    male_names = {
        "Sunday": "Kwasi",
        "Monday": "Kadjo",
        "Tuesday": "Kwabena",
        "Wednesday": "Kwaku",
        "Thursday": "Yaw",
        "Friday": "Kofi",
        "Saturday": "Kwame"
    }

    # Clean up the gender text (remove spaces, make lowercase)
    gender = gender.strip().lower()

    # If the user is female, look up the name in female_names
    # .get() returns the value for that key, or "Unknown" if missing
    if gender in ("female", "f", "girl", "woman"):
        return female_names.get(day_of_week, "Unknown")

    # If the user is male, look up the name in male_names
    elif gender in ("male", "m", "boy", "man"):
        return male_names.get(day_of_week, "Unknown")

    # If gender was not recognised at all
    else:
        return "Unknown"


def main():
    #Ask the user for info and displaying the Ashanti name

    print("=== Ashanti Day Name Finder ===\n")

    # Get the date of birth as text from the user
    dob_input = input("Enter your date of birth (dd/mm/yyyy): ")

    # Turn the text into a real date object Python understands
    date_of_birth = datetime.strptime(dob_input, "%d/%m/%Y")

    # Get the gender as text from the user
    gender = input("Enter your gender (female / male): ")

    # "%A" means "full weekday name" (Sunday, Monday, ...)
    day_of_week = date_of_birth.strftime("%A")

    # Call the function that finds the matching Ashanti name
    ashanti_name = get_ashanti_name(day_of_week, gender)

    # Show a blank line then the results
    print("\nYou were born on a " + day_of_week + ".")
    print("Your Ashanti name could have been: " + ashanti_name)


# Start the program by calling main()
main()
