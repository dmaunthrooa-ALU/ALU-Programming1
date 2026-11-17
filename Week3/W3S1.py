from datetime import datetime

#function to calculate the year in which a person will turn 100
def year_100(age):

    current_year = datetime.now().year
    years_until_100 = 100 - age
    return current_year + years_until_100


#main program asking for input
name = input('Enter your name: ')
age = int(input('Enter your age: '))

#calling function and storing results
year =year_100(age)

#Output message
print(f"Hello {name}. You will be 100 years old in the year {year}.")