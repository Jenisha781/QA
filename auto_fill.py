from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import string
import random

driver = webdriver.Edge()
url = "https://www.mindrisers.com.np/contact-us"
driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)

email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
name_field = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
phone_field = driver.find_element(By.XPATH, "//input[@placeholder='Phone']")

def generate_email():
    domain ="@abc.com"
    email_length = 5
    random_string= ''.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email = random_string + "@" + domain
    return email


def generate_name():
    return ''.join(random.choices(string.ascii_letters, k=8))
def generate_phone_number():
    return "+977-98" + ''.join(random.choices(string.digits, k=10))
d
name=generate_name()
name_field.clear()
name_field.send_keys(name)
time.sleep(2)

email = generate_email()
email_field.send_keys(email)
time.sleep(2)


phone = generate_phone_number()
phone_field.send_keys(phone)
time.sleep(2)

subject generate_subject():
subject_field.send_keys(subject)
driver.quit()