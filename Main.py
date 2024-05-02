from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Auth.PossitiveCase import loginPage

driver = webdriver.Chrome(ChromeDriverManager().install())

def Runner():
    driver.get("http://13.211.153.28:8080")
    try:
        loginPage(driver)
    finally:
        # Close the WebDriver session
        driver.quit()

if "__main__" == __name__ :
    Runner()