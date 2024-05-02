from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

User = "admin"
Password = "ZhHCzdPt8g"

def loginPage(driver: webdriver):
    wait = WebDriverWait(driver, 10)  # Define WebDriverWait object with a timeout of 10 seconds
    username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    username_input.clear()
    username_input.send_keys(User)
    password_input.clear()
    password_input.send_keys(Password)
    login_button = wait.until(EC.element_to_be_clickable((By.NAME, "submit")))
    login_button.click()
    
    