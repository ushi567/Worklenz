import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://react.worklenz.com/auth/login")

def login(email, password):
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='login_email']"))).send_keys(email)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login_password']"))).send_keys(password)
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

def verify_login_using_valid_credentials(email, password):
    login(email, password)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span[title='Assigned to me']")))
        print("Test case pass!")

    except TimeoutException :
        pytest.fail("Test case Fail - Not redirect to home page")


def verify_unable_login_using_invalid_email(email, password):
    login(email,password)

    try:
        wait.until(EC.visibility_of_element_located((By.ID,"login_email_help")))
        print("Test Case Passed! - User can't log into the Account")

    except TimeoutException :
        pytest.fail("Test case failed")


def verify_unable_login_with_empty_email(email, password):
    login(email,password)

    try:
        wait.until(EC.visibility_of_element_located((By.ID,"login_email_help")))
        print("Test Case Passed! - User can't log into the Account")

    except TimeoutException :
        pytest.fail("Test case failed")


def verify_unable_login_with_wrong_password(email, password):
    login(email,password)

    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"ant-notification-notice-description")))
        print("Test case pass!! - Error msg displayed")

    except TimeoutException():
        pytest.fail("Test case failed")






#verify_login_using_valid_credentials("ushani@ceydigital.com", "Ushi#uat567")
#verify_unable_login_using_invalid_email("ushnaiceydigital.com","gdsjer@3465")
#verify_unable_login_with_empty_email("", "")
verify_unable_login_with_wrong_password("ushani@ceydigital.com", "Ushani@5")






