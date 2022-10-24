from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import key
# from selenium.webdriver.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import time
# import Num
# Waits 1 second

#driver = webdriver.Chrome()

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
# opt.add_experimental_option("prefs", { \
#     "profile.default_content_setting_values.media_stream_mic": 1,
#     "profile.default_content_setting_values.media_stream_camera": 1,
#     "profile.default_content_setting_values.geolocation": 1,
#     "profile.default_content_setting_values.notifications": 1,
#
#
#   })
opt.add_experimental_option("prefs", {"profile.default_content_setting_values.permission": 1,
                                      "profile.default_content_setting_values.media_stream_mic": 1,
                                     "profile.default_content_setting_values.media_stream_camera": 1,
                                    "profile.default_content_setting_values.notifications": 2
                                     })
opt.add_experimental_option('excludeSwitches', ['test-type'])

driver = webdriver.Chrome(options=opts,executable_path=r'C:\Users\aksha\Downloads\chromedriver_win32\chromedriver.exe')

#driver.maximize_window()
driver.set_window_size(1000, 1000)
driver.get("https://master.dhoka4lac2b8l.amplifyapp.com")
time.sleep(5)

#xpaths =


driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-welcome-screen/div/div/div["
                              "3]/div/div/button").click()
# button = driver.find_element

time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-study-list/div/div[2]/div[1]/div/div["
                              "2]/div/div/button").click()

time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
                              "2]/div/input").send_keys("Avinash")

time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
                              "3]/div/input").send_keys(7259603078)
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
                              "4]/div/input").send_keys("ai@gmail.com")
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
                              "5]/div/div/button").click()
time.sleep(4)

driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
                              "/form/div[1]/div[1]/div/div[2]/div/input").click()

time.sleep(4)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
                              "/form/div[1]/div[2]/div/div[2]/div/input").click()

print("next page")
time.sleep(2)


driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
                              "/form/div[1]/div[3]/div/div[2]/div/input").click()


# continue button of permission screen
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div/form/div["
                              "2]/div/div/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-sample-task-success/div/div/div/div[4]/div/div/img").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-task-list/div[1]/div/div[3]/div/div/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-task-list/div[1]/div/div[2]/div/div/div/div/button").click()
time.sleep(5)

print("test completed")


