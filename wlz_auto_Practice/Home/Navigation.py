
import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
wait   = WebDriverWait(driver,timeout=10)
driver.get("https://react.worklenz.com/auth/login")

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='login_email']"))).send_keys('yevsyynv73@qzueos.com')
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='login_password']"))).send_keys('Yevs@123')
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[title ='Assigned to me']")))
time.sleep(3)

def navigation_to_projects_tab():
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Projects"))).click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-page-header-heading-title css-avcqrf")))
    print("Test case pass!!!")


navigation_to_projects_tab()
