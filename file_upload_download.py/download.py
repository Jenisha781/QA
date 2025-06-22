from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = "https://filebin.net/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

file_upload_button = driver.find_element(*(By.XPATH, "//input[@id='fileField']"))
file_upload_button.send_keys("C:/Users/karma/Pictures/Screenshots/Screenshot%202025-06-10%20113701.png")
driver.quit()  # Replace with the actual file path

more_options_button = driver.find_element(By.XPATH, "//button[@id='moreOptions']")
more_options_button.click()
time.sleep(2)

download_link = driver.find_element(By.XPATH, "//button[@id='download']")
download_link.click()
time.sleep(5)  # Wait for the download to complete

driver.quit()
