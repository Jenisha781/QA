from selenium import webdriver
import time
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

#from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager


#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver=webdriver.Edge()

url = "https://www.google.com"
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.quit()
