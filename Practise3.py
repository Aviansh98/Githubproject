from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import key
# from selenium.webdriver.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time
# Waits 1 second

#driver = webdriver.Chrome()

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
  })

driver = webdriver.Chrome(options=opt, executable_path=r'C:\Users\aksha\Downloads\chromedriver_win32\chromedriver.exe')

#driver.maximize_window()
driver.set_window_size(1000, 1000)
driver.get("https://participants-integration.userstudy.co/")
time.sleep(5)
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
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
                              "4]/div/input").send_keys("ai@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
                              "5]/div/div/button").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
                              "/form/div[1]/div[1]/div/div[2]/div/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
                              "/form/div[1]/div[2]/div/div[2]/div/input").click()
# #code to give permission for use for camera and mic
# desired_cap = {
#          'browser_version': '104.0.5112.101',
#          'os': 'Windows',
#          'os_version': '10',
# # # var caps = new ChromeOptions();
# # #
# # # caps.PlatformName = "Mac OSX 10.15";
# # # caps.BrowserVersion = "84";
# # # caps.AddAdditionalCapability("username", username, true);
# # # caps.AddAdditionalCapability("password", authkey, true);
# # #Configure ChromeOptions to pass fake media stream
#         'chromeOptions': {
#     'args': ["--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream"]
#   }
# }
# driver = webdriver.Remote(command_executor = 'http://avinash_FWHOef:scKzncFzBydqfLKqxphp@hub.browserstack.com/wd/hub', options=webdriver.ChromeOptions())
# # driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',options=webdriver.ChromeOptions())

# driver.get('http://www.google.com/')
# WebCam Test
print("next page")

time.sleep(2)
#driver.find_element(By.XPATH, "webcam-launcher").click()


# # Mic Test
# driver.get("https://www.vidyard.com/mic-test/")
# time.sleep(5)
# driver.find_element(By.XPATH, "//a[@id='start-test']").click()
# time.sleep(10)



# ChromeOptions options = new Chromeoption()
# options.addargument("disable use for camera");
# driver = new Chromeoptions();
# time.sleep(5)
# thrid toggle button

time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div/form/div[1]/div[3]/div/div[2]/div/input").click()

# continue button of permission screen
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div/form/div["
                              "2]/div/div/button").click()

# driver.close()
#driver.quit()
print("test completed")

print("test")

