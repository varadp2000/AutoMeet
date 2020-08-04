'''
Auto google meet joining bot using Selenium Web Driver, Python and Google Chrome
Use Gmail ID with no 2Factor Auth
Works only with Google Meet
Use Time Format as HH:MM
Always provide time duration in minutes
To stay safe from late joining, Enter joining time 5 min earlier for 1st Meet
Can't run multiple meets at same time
Default Timezone: Asia/Kolkata GMT + 5:30

Dependencies:
Selenium
webdriver_manager
    pip install selenium
    pip install webdriver_manager
Webdriver manager automatically handels Chrome driver for Selenium(takes more time on 1st load of program per machine)

ChromeDriver For Google Chrome 84 is kept for backup purpose

'''


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import datetime
from selenium.webdriver.chrome.options import Options
import pytz

chrome_options = Options()

chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("disable-popup-blocking")

chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })

username = input("Enter Email\n")
password = input("Enter Password\n")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
def scheduler():
    for i in range (0,t):
        temp = []
        temp.append(input("Enter Link"))
        temp.append(input("Enter Time(HH:MM)24HRS"))
        temp.append(float(input("Enter Duration")))
        arr.append(temp)

t = int(input("Enter No of lecs"))
arr = []

def send_key(winid, key):
    xdotool_args = ['xdotool', 'windowactivate', '--sync', winid, 'key', key]
    subprocess.check_output(xdotool_args)

TIMEZONE = pytz.timezone("Asia/Calcutta")
def get_waiting_time(TIMEZONE, time):
    now = datetime.datetime.now(tz=TIMEZONE).replace(tzinfo=None)
    curr_time = now.time()
    curr_date = now.date()
    bkp_time = datetime.datetime.strptime(time,"%H:%M").time()
    bkp_datetime = datetime.datetime.combine(curr_date, bkp_time)

    bkp_minus_curr_seconds = (bkp_datetime - now).total_seconds()
    a_day_in_seconds = 60 * 60 * 24
    wait_time = a_day_in_seconds + bkp_minus_curr_seconds if bkp_minus_curr_seconds < 0 else bkp_minus_curr_seconds

    return wait_time

def login():
    driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    driver.implicitly_wait(5)

    driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    driver.implicitly_wait(15)
    time.sleep(7)        #precaution for slow network
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()


scheduler()
login()
arr = sorted(arr, key=lambda x:x[1])

#Debug:
#meetList = ["https://meet.google.com/vtw-hxuw-abm", "https://meet.google.com/hgs-txhy-brd", "https://meet.google.com/hgs-txhy-brd"]

for meet in arr:
    time.sleep(get_waiting_time(TIMEZONE, meet[1]))
    driver.get(meet[0])
    time.sleep(5)

    if driver.current_url.find("AccountChooser") != -1:
        print(driver.current_url.find("AccountChooser"))
        driver.find_element_by_xpath('//*[@id="profileIdentifier"]').click()
    time.sleep(2)
    driver.get(meet[0])
    time.sleep(2)
    driver.get(meet[0])

    try:
        driver.find_element_by_xpath('//span[text()="Dismiss"]')
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except:
        pass

    try:
        driver.find_elements_by_xpath("//*[text()='Ask to join']")[0].click()
    except:
        pass

    try:
        driver.find_elements_by_xpath("//*[text()='Join now']")[0].click()
    except:
        pass
    print("Here")
    time.sleep(60)
#for meet in meetList:
#    driver.get(meet)
#    time.sleep(10)

#passw=open('New Text Document (2).txt',"r",encoding="utf-8")   
#user=open('New Text Document (3).txt',"r",encoding="utf-8")   

'''
©VaradPatil
https://github.com/varadp2000/AutoMeet

Hist:
    02/08/2020: Development Begien
    04/08/2020: Development Finished(Beta Testing)
'''
