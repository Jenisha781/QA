from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = "https://www.saucedemo.com"
driver.get(url)
driver.maximize_window()
time.sleep(5)

username_field = driver.find_element (By.ID,"user-name")
username_field.send_keys("standard_user")
time.sleep(4)
password_field = driver.find_element(By.NAME,"password")
password_field.send_keys("secret_sauce")
time.sleep(2)

login_button = driver.find_element(By.ID,"login-button")
login_button.click()
time.sleep(5)

current_url = driver.current_url
if current_url == "https://www.saucedemo.com/inventory.html":
 print("Login successful.")
else:
 print("Login failed")

driver.quit()