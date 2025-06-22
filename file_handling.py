from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = "https://formy-project.herokuapp.com/form.com"
driver.get(url)
driver.maximize_window()
time.sleep(5)

first_name_field = driver.find_element(By.XPATH,"//input[@id='first-name']")
first_name_field.send_keys("John")
time.sleep(2)
last_name_field = driver.find_element(By.XPATH,"//input[@id='last-name']")
last_name_field.send_keys("Doe")
time.sleep(2)
job_title_field = driver.find_element(By.XPATH, "//input[@id='job-title']")
job_title_field.send_keys("QA Engineer")
time.sleep(2)


driver.quit()
