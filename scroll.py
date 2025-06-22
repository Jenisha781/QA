from selenium import webdriver
import time

driver=webdriver.Edge()
url = "https://www.triphimalaya.com"
driver.get(url)
driver.maximize_window()
time.sleep(5)

#driver.execute_script("window.scrollBY(0,-2000);")
#time.sleep(1)

#document_height = driver.execute_script("return document.body.scrollHeight")
scroll_speed =  500
scroll_iterations = int(document_height/scroll_speed)
for _ in range(scroll_iterations):
driver.execute_script("window.scrollBY(0,500);")
time.sleep(0.5)


driver.quit()