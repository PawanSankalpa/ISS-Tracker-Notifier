import requests
import datetime as dt
import smtplib
import time
import os
from dotenv import load_dotenv

"""Load your credentials from the .env"""
load_dotenv()

"""_____________________Editor's Panel__________________________"""
MY_LATITUDE = os.getenv("LATITUDE")
MY_LONGITUDE = os.getenv("LONGITUDE")
MARGIN_OF_ERROR = 5

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("APP_PASSWORD")
print(MY_PASSWORD)
RECEIVER_EMAIL = "pawansankalpanew123@gmail.com"
#----------------------------------------------------------------#
"""_____________________Variables__________________________"""
my_location_err_plus = MY_LATITUDE+MARGIN_OF_ERROR , MY_LONGITUDE+MARGIN_OF_ERROR
my_location_with_err_minus = MY_LATITUDE-MARGIN_OF_ERROR , MY_LONGITUDE-MARGIN_OF_ERROR

#----------------------------------------------------------------#
"""_________function :iss location____________"""
def iss_location():
    response_iss = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = data_iss["iss_position"]["latitude"]
    iss_longitude = data_iss["iss_position"]["longitude"]
    return float(iss_latitude) , float(iss_longitude)

#----------------------------------------------------------------#
"""_________function dark or not____________"""
def dark_or_not():
    now = dt.datetime.now()
    # current_time = now.time()   #value =  13:02:58.388032 \int
    # current_time = str(current_time).split(":")  #value = ['13','02','58.388032'] \list
    # current_time = f"{current_time[0]}:{current_time[1]}" #value = 13:02 \str
    '''instead of all of these steps we can simply use strftime method'''
    current_time = now.strftime("%H:%M")
    current_time = int(current_time.replace(":",""))

    if current_time >= 1800 or current_time <= 530 :
        return "dark"
    else:
        return "not dark"

#----------------------------------------------------------------#
"""_________function : text send____________"""
def text_send():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = RECEIVER_EMAIL,
            msg = "International Space Station is here\n\n'Look Up!'"
        )

#----------------------------------------------------------------#
"""_________if its dark then check iss lat and long,____________"""
while True: # running nonstop in the background as long as the sever is on
    time.sleep(60) # execute this code every 60 seconds
    surrounding = dark_or_not()
    if surrounding == "dark":

        '''----assigning all the values----------'''
        iss_lat = iss_location()[0]
        iss_lng = iss_location()[1]
        my_minus_lat = my_location_with_err_minus[0]
        my_minus_lng = my_location_with_err_minus[1]
        my_plus_lat = my_location_err_plus[0]
        my_plus_lng = my_location_err_plus[1]
        #-------------------------------------------#

        if my_plus_lat > iss_lat > my_minus_lat and my_plus_lng > iss_lng > my_minus_lng:
            text_send()

#------------------------------------------------------------------------------#

