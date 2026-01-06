#function to check wether, run the function first, then it's call!
def check_weather():
    temperature=16
    if temperature > 25:
        print("It's a hot day.")
    else:
        print("Cool day")

check_weather()
#date and time library to know the time live
import datetime

today= datetime.datetime.now()
print(today)

#importing the operatin system
import os

current_dir= os.getcwd()
print(current_dir)

import json
date={"name":"John", "age":30}
json_string=json.dumps(date)