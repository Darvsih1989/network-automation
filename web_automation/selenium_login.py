from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

url = "https://example.com/login"
username = "your_username"
password = "your_password"

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

try:
    driver.get(url)
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Login attempted")

finally:
    driver.quit()