import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
wait = WebDriverWait(driver,timeout=10)
driver.get("https://react.worklenz.com/auth/login")
time.sleep(2)


forgot_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Forgot password?"))).click()

def verify_forgot_password():
    try:
        wait.until(EC.visibility_of_element_located((By.ID,"forgot-password_email")))
        print("Test case passed - Redirected to the Password Reset Page")

    except TimeoutException:
        pytest.fail("Test case fail")


def verify_Reset_the_password():
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='forgot-password_email']"))).send_keys("malkiis283@gmail.com")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']")))
        print("Test case passed - Reset password link was sent to the email!!")

    except TimeoutException:
        pytest.fail("Test case fail")


def verify_Return_to_login():
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Return to Login"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='login_email']")))
        print("Test case passed - Redirected to the login page!!")

    except TimeoutException:
        pytest.fail("Test case fail")


def verify_Reset_password_using_invalid_email():
    try:
       wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'forgot-password_email']"))).send_keys("malkigmail")
       time.sleep(5)
       wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"ant-form-item-explain-error")))
       print("Test case passed!! - User can't reset the password")

    except TimeoutException:
        pytest.fail("Test case fail")


def verify_Reset_password_with_Empty_field():

    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id = 'forgot-password_email']"))).send_keys("")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']"))).click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ant-form-item-explain-error")))
        print("Test case pass!! - Error msg displayed")

    except TimeoutException:
        pytest.fail("Test case failed")










#verify_forgot_password()
#verify_Reset_the_password()
#verify_Return_to_login()
#verify_Reset_password_using_invalid_email()
verify_Reset_password_with_Empty_field()