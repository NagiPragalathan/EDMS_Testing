from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


User = "admin"
Password = "ZhHCzdPt8g"

@pytest.mark.usefixtures("driver")
def loginPage(driver, User=User, Password=Password):
    wait = WebDriverWait(driver, 10)  # Define WebDriverWait object with a timeout of 10 seconds
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    
    assert username_input.is_displayed(), "Username input field is not displayed"
    assert password_input.is_displayed(), "Password input field is not displayed"
    
    username_input.clear()
    username_input.send_keys(User)
    password_input.clear()
    password_input.send_keys(Password)
    
    assert username_input.get_attribute("value") == User, "Username input is incorrect"
    assert password_input.get_attribute("value") == Password, "Password input is incorrect"
    
    login_button = wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
    
    assert login_button.is_enabled(), "Login button is not clickable"
    
    login_button.click()

    
    