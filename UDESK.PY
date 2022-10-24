from selenium import webdriver
print("hi")
from selenium.webdriver.common.keys import Keys
print("keys")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver..options import Options
print("by")

print(1)
from selenium.webdriver.chrome.service import Service
import time
# options = webdriver.ChromeOptions()
# print(3)
#
# loggingPrefs = { "driver": "INFO", "browser": "INFO" }
# print(4)
# options.set_capability("goog:chromeOptions", {"performance": "ALL"})
# print(5)
# service = ChromeService(executable_path=r"C:\Users\aksha\Downloads\chromedriver_win32 (1)\chromedriver")
# print(6)

# driver = webdriver.Chrome(service=ser)
# print(7)
serv_obj=Service(r"C:\Users\aksha\Downloads\chromedriver_win32 (1)\chromedriver")

driver=webdriver.Chrome(service=serv_obj)
driver.get("https://master.d3rba50cxdreo3.amplifyapp.com/login")
# driver.get("https://staging.d3rba50cxdreo3.amplifyapp.com/login?return=%2Fdashboard%2Fstudies")
driver.maximize_window()

print("smile pls")
time.sleep(3)
print("Hlo")
driver.find_element(By.ID,"email").send_keys('mehetreavinash345@gmail.com')
print("By")
time.sleep(3)
driver.find_element(By.ID,"password") .send_keys("5854@Avi!")
print("password")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-login/div/div/div/div/div[2]/form/div/div[3]").click()
print("click")

time.sleep(4)
# Studies_Page_Code
# driver.get("https://master.d3rba50cxdreo3.amplifyapp.com/dashboard/studies")
# driver.find_element(By.XPATH,"/html/body/app-root/div[1]/div/app-dashboard/div[1]/div[2]/div[1]")

# driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-dashboard/div[1]/div[2]/div[2]/div/app-studies/div[1]/div/div/div[2]/div/div/div[1]/div/div/input").send_keys("Mehetre 1st Workspace")
driver._switch_to_frame(driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-dashboard/div[1]/div[2]/div[1]"))
print("menu")

print("Yes")
driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-dashboard/div[1]/div[2]/div[1]/div[2]/app-side-menu/div/div[1]/ul/li[1]/div/div").click()
driver._switch_to_frame(driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-dashboard/div[1]/div[2]/div[2]/div"))

print("recording")
driver.find_element(By.XPATH,"/html/body/app-root/div[1]/div/app-dashboard/div[1]/div[2]/div[2]/div/app-studies/div[1]/div/div/div[4]/div/div[1]/div/div").click()
time.sleep(5)
# import pdb
# pdb.set_trace()
driver.find_element(By.XPATH, "/html/body/app-root/div[1]/div/app-dashboard/div[1]/div[2]/div[2]/div/app-studies/div[1]/div/div/div[4]/div/div[1]/div/div").click()
print("box")

# # Create_Study_Button
# print("create study")
# driver.find_element(By.XPATH,"/html/body/app-root/div[1]/div/app-dashboard/div[1]/div[2]/div[2]/div/app-studies/div[1]/div/div/div[4]/div/div[1]").click()
# print("end")
# print(5)
# time.sleep(4)
# driver.find_element(By.XPATH, "//*[@id=='studiespopup']/ngb-modal-window/div/div/app-study-modal/div[2]/div/div/div[1]/div/label").click()
# time.sleep(4)
# driver.find_element(By.Xpath, "//*[@id='studiespopup']/ngb-modal-window/div/div/app-study-modal/div[3]/app-form-button/button"). click()
# time.sleep(4)
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-basic"
#                                "-requirements/div/form/div/div[1]/div[2]").send_Keys('amazon prout percharse study')
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-basic-requirements"
#                               "/div/form/div/div[2]/div[2]/div/div[2]/div/label/div"). Click()
# time.sleep(4)
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-dashboard/div[1]/div[2]/div[2]/div/app-studies/div[1]/div/div/div[4]"
#                               "/div/div[1]/div/div"). Click()
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-basic-requirements/div/form/div/div[3]/div[2]/div[1]/div[2]/div/label/div").click()
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-basic-requirements/div/form/div/div[3]/div[2]/div[1]/div[3]/div/label/div").Click()
# time.sleep(4)
# # Continue_button
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[3]/div/div/div/div/div/app-form-button/button").Click()
# time.sleep(4)
# # Welcome_Screen
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-task-information/form/div/div[1]/div[2]/div/textarea").send_keys('welcome to AMAZON')
# Sleep.time(4)
# # landing_page_URL
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-task-information/form/div/div[2]/div[2]/div/div/input"). send_keys('https://www.amazon.in/')
# # Task1
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-task-information/form/div/div[3]/div[1]/div/div/div[1]/div/textarea").send_keys('select one product')
# time.sleep(4)
# # Task_URL
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-task-information/form/div/div[3]/div[1]/div/div/div[2]/div/input").send_key('https://www.amazon.in/')
# time.sleep(4)
# # Add_task_Button
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-task-information/form/div/div[3]/div[2]/div/div").Click()
# time.sleep(4)
# # Task2
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-task-information/form/div/div[3]/div[1]/div[2]/div/div[1]/div/textarea").send_keys('Add in to Cart')
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-task-information/form/div/div[3]/div[1]/div[2]/div/div[2]/div/input"). Send_keys('https://www.amazon.in/')
# time.sleep(4)
# # Final Screen of task_page
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-task-information/form/div/div[4]/div[2]/div/textarea"). send_keys('thank you participant')
# # Adding Task_page Continue BUtton
# time.sleep(4)
# driver.find_element(By.Xpath,"/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[3]/div/div/div/div/div/app-form-button/button").click()
# time.sleep(4)
# # Finish_Screen_copy_button
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[2]/div/app-invite-participants/div/div[2]/div/div/div/div/div/div[1]"). click()
# time.sleep(4)
# # Finish_Button
# driver.find_element(By.Xpath, "/html/body/app-root/div[1]/div/app-layout/div/div[2]/div/app-create-study/div/div/div[3]/div/div/div/div/div/app-form-button/button"). Click