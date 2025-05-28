import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
wait = WebDriverWait(driver,timeout=10)
driver.get("https://react.worklenz.com/auth/login")

def login(email):
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='login_email']"))).send_keys(email)
    driver.find_element(By.LINK_TEXT,"Forgot password?").click()

def verify_login_forgot_password_page(email):
    login(email)
    try:
        wait.until(EC.visibility_of_element_located((By.ID,"forgot-password_email")))
        print("Test case pass!")

    except TimeoutException:
        pytest.fail("Test case fail")




#login("ushani@ceydigital.com")
verify_login_forgot_password_page("ushani@ceydigital.com")


