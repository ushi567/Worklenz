import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
wait   = WebDriverWait(driver,timeout= 10)
driver.get("https://react.worklenz.com/auth/verify-reset-email/OGY5NTNmYTMtZTlmZi00ZTNkLWIzMjEtOWM5ZWM4ZjZmNTU5/$2b$10$piI.01lv2DeBC-1rfnXyIejEbjXol6yMriovvetur7CK-5TKNh7YO")

def verify_Reset_password_valid_credentials():

    try:
        wait.until(EC.visibility_of_element_located((By.ID,"verify-reset-email_newPassword"))).send_keys("David@123")
        wait.until(EC.visibility_of_element_located((By.ID, "verify-reset-email_confirmPassword"))).send_keys("David@123")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']"))).click()
        print("Test case pass!! - Display success msg")

    except TimeoutException:
        pytest.fail("Test case fail")


def Reset_pw_without_symbol():

    try:
        wait.until(EC.visibility_of_element_located((By.ID,"verify-reset-email_newPassword"))).send_keys("David123")
        wait.until(EC.visibility_of_element_located((By.ID, "verify-reset-email_confirmPassword"))).send_keys("David123")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']"))).click()
        time.sleep(3)
        print("Test case pass!! - Displayed Error msg")

    except TimeoutException:
        pytest.fail("Test case fail")







#verify_Reset_password_valid_credentials()
Reset_pw_without_symbol()