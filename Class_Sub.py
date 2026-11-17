#importing datetime Library
from datetime import datetime

 #function1 : fining the day the user was born from his DOB
 def get_day_week(date_of_birth):
     return date_of_birth.weekday.strftime("%a")

 #function 2
 def get_ashanti_name(day_week,gender):

     gender = gender.s