from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", {"profile.default_content_setting_values.permission": 1,
                                      "profile.default_content_setting_values.media_stream_mic": 1,
                                      "profile.default_content_setting_values.media_stream_camera": 1,
                                      "profile.default_content_setting_values.notifications": 2
                                      })
opt.add_experimental_option('excludeSwitches', ['test-type'])
# options=opt, executable_path=r'C:\Users\aksha\Downloads\chromedriver_win32\chromedriver.exe

s = Service(r"C:\Users\aksha\Downloads\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
driver.set_window_size(1000, 1000)
driver.get("https://master.dhoka4lac2b8l.amplifyapp.com/participant")
time.sleep(5)
# /html/body/app-root/div/div/div/div/app-welcome-screen/div/div/div[3]/div/div/button
paths = [
    "/html/body/app-root/div/div/div/div/app-welcome-screen/div/div/div[3]/div/div/button",
    "/html/body/app-root/div/div/div/div/app-study-list/div/div[2]/div[1]/div/div["
    "2]/div/div/button",
    "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
    "2]/div/input",
    "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
    "3]/div/input",
    "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
    "4]/div/input",
    "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
    "5]/div/div/button",
    "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
    "/form/div[1]/div[1]/div/div[2]/div/input",
    "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
    "/form/div[1]/div[2]/div/div[2]/div/input",
    "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
    "/form/div[1]/div[3]/div/div[2]/div/input",
    "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div/form/div["
    "2]/div/div/button",
    "/html/body/app-root/div/div/div/div/app-sample-task-success/div/div/div/div["
    "4]/div/div/img"
    "/html/body/app-root/div/div/div/div/app-task-list/div[1]/div/div[3]/div/div/button",
    "/html/body/app-root/div/div/div/div/app-task-list/div[1]/div/div["
    "2]/div/div/div/div/button"
]
sendKeys = ["Avinash", "7259603078", "ai@gmail.com"]
index = 0
for x in paths:
    if "input" in x:
        #print("avi")
        #print(x)
        time.sleep(3)
        driver.find_element(x).send_keys(sendKeys[index])
        print(sendKeys[index])
        index = index + 1
        # print("++++")
        # driver.find_element(x).send_keys(sendKeys[index])
        time.sleep(5)
    else:
        driver.find_element(x).click()
print("test completed")
