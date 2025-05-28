from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver,10)

driver.get("https://react.worklenz.com/auth/login")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='login_email']"))).send_keys("ushani@ceydigital.com")
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='login_password']"))).send_keys("Ushi#uat567")

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='Submit']")))




