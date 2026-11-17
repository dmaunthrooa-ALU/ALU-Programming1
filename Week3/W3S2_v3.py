# Import the datetime class so we can work with real dates
from datetime import datetime

def parse_date(user_input):
    text = user_input.strip()
    formats = [
        "%d/%m/%Y", "%d-%m-%y", "%d.%m.%Y", "%d %m %Y",
        "%d%m%Y", "%d %b %y", "%d %B %Y", "%d-%B-%Y",
        "%d/%b/%Y", "%d/%B/%Y", "%Y-%m-%d", "%Y/%m/%d",
        "%Y.%m.%d", "%m/%d/%Y", "%m-%d-%Y"
    ]
    for f in formats:
        try:
            return datetime.strptime(text, f)
        except ValueError:
            continue
    return None  # Must be outside the loop


def get_day_of_week(day_of_birth):
    return day_of_birth.strftime("%A")


def get_ashanti_name(day_of_week, gender):
    # Return the Ashanti day name using two lookup tables

    # Dictionary that maps each weekday to its female name
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

    if gender in ("female", "f", "girl", "woman"):
        return female_names.get(day_of_week, "Unknown")
    elif gender in ("male", "m", "boy", "man"):
        return male_names.get(day_of_week, "Unknown")
    else:
        return "Unknown"


def main():
    print("Ashanti Name Finder\n")

    date_of_birth = None
    while date_of_birth is None:          # 'while' must be lowercase
        dob_input = input("Enter your date of birth: ")
        date_of_birth = parse_date(dob_input)
        if date_of_birth is None:
            print("Please enter a valid date of birth.\n")

    gender = input("Enter your gender (Male / Female): ")
    day = get_day_of_week(date_of_birth)
    name = get_ashanti_name(day, gender)

    print("\nYou were born on a " + day + ".")
    print("Your Ashanti name could have been: " + name)


main()