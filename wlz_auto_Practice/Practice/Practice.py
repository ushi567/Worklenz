import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://react.worklenz.com/auth/login")
driver.maximize_window() #maximize Web page
time.sleep(5)

driver.find_element(By.XPATH, "//input[@id='login_email']").send_keys('ushani@ceydigital.com')
driver.find_element(By.XPATH, "//input[@id='login_password']").send_keys('Ushani@123')
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

