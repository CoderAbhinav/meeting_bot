import meeting_platforms as mp
import pause
import pandas as pd
from datetime import datetime
import time 

mp.take_credentials('dumm','dum')
mp.change_driver_path('chromedriver')
mp.change_profile_path("/home/abhinav/.config/google-chrome")

def list_of_date_time(raw_date, raw_time):
    raw_date = raw_date.split("-")
    raw_date = list(map(int, raw_date))
    raw_date.reverse()

    raw_time = raw_time.split(":")
    raw_time = list(map(int ,raw_time))

    final_list = raw_date + raw_time
    return final_list


df = pd.read_csv("timings.csv")
i = 0
while i < df.shape[0]:
    info = df.iloc[i]

    date_is = str(info[0])
    time_is = str(info[1])
    link_is = str(info[2])
    id_is = str(info[3])
    psw_is = str(info[4])

    event_schedule = list_of_date_time(date_is, time_is)
    # print(*event_schedule)
    if datetime(*event_schedule)<datetime.now():
        i+=1
        continue

    print("Upcoming Meeting Information : ")
    print(info)

    pause.until(datetime(*event_schedule))
    
    print("Starting the above meeting")

    if 'meet' in link_is:
        mp.google_meet(link_is)

    elif 'zoom' in link_is:
        mp.zoom(link_is)

    elif pd.isnull(info[2]):
        if id_is.isdigit():
            mp.zoom_by_id(id_is, psw_is)

        elif id_is.isalpha():
            mp.google_meet_by_id(id_is)

    df = pd.read_csv("timings.csv")

    i+=1
