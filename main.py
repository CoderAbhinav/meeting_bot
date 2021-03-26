from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pause
import pyautogui
import pandas as pd
import webbrowser

from datetime import datetime
import time 

my_mail_id = ''
my_password = ''

def google_meet_with_gmail_login(meet_url):
    global my_mail_id
    global my_password
    mail_address = my_mail_id
    password = my_password
    opt = webdriver.ChromeOptions() 
    opt.add_argument('--disable-blink-features=AutomationControlled') 
    opt.add_argument('--start-maximized') 
    opt.add_experimental_option("prefs", { 
	"profile.default_content_setting_values.media_stream_mic": 1, 
	"profile.default_content_setting_values.media_stream_camera": 1, 
	"profile.default_content_setting_values.geolocation": 0, 
	"profile.default_content_setting_values.notifications": 1
    })

    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=opt)
    driver.get("https://google.com") 
    driver.maximize_window()
    # going to Gmail Login Page
    driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

    # input Gmail 
    driver.find_element_by_id("identifierId").send_keys(mail_address) 
    driver.find_element_by_id("identifierNext").click() 
    driver.implicitly_wait(10) 
    
    # input Password 
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password) 
    driver.implicitly_wait(10) 
    driver.find_element_by_id("passwordNext").click() 
    driver.implicitly_wait(100)
    
    time.sleep(2)

    # going to google meet link
    driver.get(meet_url) 
    wait = WebDriverWait(driver, 10)    
    
    # turn off mic
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME ,'sUZ4id' ))).click()
    driver.implicitly_wait(3)
    
    # turn off camera 
    driver.find_elements_by_class_name('sUZ4id')[1].click()
    driver.implicitly_wait(3) 
    time.sleep(2)

    #click on join button
    driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    input("press any key to stop program")
    


def google_meet_with_profile(meet_url):
    
    options = webdriver.ChromeOptions() 
    options.add_argument("--user-data-dir=C:\\Users\\keyur\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
    options.add_argument('--profile-directory=Default') #give your profile
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    driver.get("https://google.com") 
    driver.maximize_window()
    

    # going to google meet link
    driver.get(meet_url) 
    wait = WebDriverWait(driver, 10)    
    
    # turn off mic
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME ,'sUZ4id' ))).click()
    driver.implicitly_wait(3)
    
    # turn off camera 
    driver.find_elements_by_class_name('sUZ4id')[1].click()
    driver.implicitly_wait(3) 
    time.sleep(2)

    #click on join button
    emailid = driver.find_element_by_css_selector('div.ASy21.Duq0Bf')
    print(emailid.text)
    if not (emailid.text.endswith("@viit.ac.in")):
        driver.quit()
        raise Exception("Wrong Email Exception")

    
def google_meet(meeting_url):
    try:
        google_meet_with_profile(meeting_url)
    except Exception as e:
        print(e)
        google_meet_with_gmail_login(meeting_url)


def google_meet_by_id(meeting_id):
    url = f"http://meet.google.com/{meeting_id}"
    google_meet(url)

def zoom(zoom_url):
   webbrowser.open(zoom_url)


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
    print(*event_schedule)
    if datetime(*event_schedule)<datetime.now():
        i+=1
        continue

    print("Upcoming Meeting Information : ")
    print(info)

    pause.until(datetime(*event_schedule))
    
    print("Starting the above meeting")

    if 'meet' in link_is:
        google_meet(link_is)

    elif 'zoom' in link_is:
        zoom(link_is)

    elif pd.isnull(info[2]):
        if id_is.isdigit():
            zoom_by_id(id_is, psw_is)

        elif id_is.isalpha():
            google_meet_by_id(id_is)

    df = pd.read_csv("timings.csv")

    i+=1
