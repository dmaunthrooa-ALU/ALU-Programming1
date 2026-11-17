# Import the datetime class so we can work with real dates
from datetime import datetime

# FUNCTION 1: Find the day of the week from a date object
def get_day_of_week(date_of_birth):
    # Return the English name of the weekday (e.g. "Sunday")
    # strftime converts a date into a formatted string
    # "%A" is the format code for the full weekday name
    return date_of_birth.strftime("%A")


# FUNCTION 2: Look up the Ashanti name from day + gender
def get_ashanti_name(day_of_week, gender):
    #Return the traditional Ashanti day name

    # Remove extra spaces and make everything lowercase
    # so "Female", "FEMALE", " female " all become "female"
    gender = gender.strip().lower()

    # Check whether the user said they are female
    if gender in ("female", "f", "girl", "woman","lady"):
        # Now check which day of the week it is
        if day_of_week == "Sunday":
            return "Akosua"
        elif day_of_week == "Monday":
            return "Adwoa"
        elif day_of_week == "Tuesday":
            return "Abeena"
        elif day_of_week == "Wednesday":
            return "Akwa"
        elif day_of_week == "Thursday":
            return "Yaa"
        elif day_of_week == "Friday":
            return "Afia"
        elif day_of_week == "Saturday":
            return "Amma"


    # Check whether the user said they are male
    elif gender in ("male", "m", "boy", "man"):
        if day_of_week == "Sunday":
            return "Kwasi"
        elif day_of_week == "Monday":
            return "Kadjo"
        elif day_of_week == "Tuesday":
            return "Kwabena"
        elif day_of_week == "Wednesday":
            return "Kwaku"
        elif day_of_week == "Thursday":
            return "Yaw"
        elif day_of_week == "Friday":
            return "Kofi"
        elif day_of_week == "Saturday":
            return "Kwame"

    # If gender or day did not match anything above
    return "Unknown"


# MAIN PROGRAM
def main():
    #Asking the user for info and displaying the corresponding Ashanti name

    # Print a title (\n adds a blank line after)
    print("=== Ashanti Day Name Finder ===\n")

    # Ask the user to type their date of birth
    # The answer is always stored as a string
    dob_input = input("Enter your date of birth (dd/mm/yyyy): ")

    # Convert the text "05/11/2000" into a real date object
    # "%d/%m/%Y" tells Python the order is day/month/year
    date_of_birth = datetime.strptime(dob_input, "%d/%m/%Y")

    # Ask the user for their gender
    gender = input("Enter your gender (female / male): ")

    # Call our first function to get the weekday name
    day_of_week = get_day_of_week(date_of_birth)

    # Call our second function to get the Ashanti name
    ashanti_name = get_ashanti_name(day_of_week, gender)

    # Print a blank line and a separator for clean output
    print("\n----------------------------------------")

    # Tell the user which day they were born on
    # The + sign joins the pieces of text together
    print("You were born on a " + day_of_week + ".")

    # Tell the user the Ashanti name
    print("Your Ashanti name could have been: " + ashanti_name)

# This line actually starts the programIt calls the main() function we defined above
main()
