from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time


driver=webdriver.Firefox()
driver.get("https://my.asrez.com/login")

elem=driver.find_element(By.ID,"email")
elem.clear()
elem.send_keys("09935020470")



elem=driver.find_element(By.ID,"password")
elem.clear()
elem.send_keys("1250903785")


elem=driver.find_element(By.CSS_SELECTOR,"body > div.main-container.min-h-screen.text-black.dark\:text-white-dark > div > div > form > button")
elem.click()
elem.sleep()




