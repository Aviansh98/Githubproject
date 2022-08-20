
import time
# Waits 1 second

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://participants-integration.userstudy.co/")
time.sleep(10)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-welcome-screen/div/div/div["
                              "3]/div/div/button").click()
# button = driver.find_element

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-study-list/div/div[2]/div[1]/div/div["
                              "2]/div/div/button").click()

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
                              "2]/div/input").send_keys("Avinash")

time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
                              "3]/div/input").send_keys(7259603078)
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
                              "4]/div/input").send_keys("ai@gmail.com")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-add-tester-details/div/form/div/div["
                              "5]/div/div/button").click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
                              "/form/div[1]/div[1]/div/div[2]/div/input").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
                              "/form/div[1]/div[2]/div/div[2]/div/input").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div"
                              "/form/div[1]/div[3]/div/div[2]/div/input").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/app-enable-microphone-camera/div/div/div/form/div["
                              "2]/div/div/button").click()

#driver.close()
#driver.quit()
print("test completed")

print("test")

