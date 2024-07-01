from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time


driver=webdriver.Firefox()
driver.get("https://my.asrez.com/register")

elem=driver.find_element(By.ID ,"first_name")
elem.clear()
elem.send_keys("fateme")

time.sleep(1)

elem=driver.find_element(By.ID ,"last_name")
elem.clear()
elem.send_keys("karimshahi")

time.sleep(1)

elem=driver.find_element(By.ID ,"email")
elem.clear()
elem.send_keys("fkarimshahi.86.4@gmail.com")

time.sleep(1)

elem=driver.find_element(By.ID ,"github_id")
elem.clear()
elem.send_keys("https://github.com/dashboard")

time.sleep(1)

elem=driver.find_element(By.ID ,"landline_number")
elem.clear()
elem.send_keys("03155339050")

time.sleep(1)

elem=driver.find_element(By.ID ,"address")
elem.clear()
elem.send_keys("khashan")

time.sleep(1)

elem=driver.find_element(By.ID ,"national_code")
elem.send_keys("1250903759")

time.sleep(1)

elem=driver.find_element(By.ID ,"postal_code")
elem.clear()
elem.send_keys("33157444145")

time.sleep(1)

elem=driver.find_element(By.ID ,"wakatime_token")
elem.send_keys("https://wakatime.com/@71f184ee-1c0d-403f-a671-ef7708bf7769")

time.sleep(1)

elem=driver.find_element(By.ID ,"telegram_id")
elem.send_keys("https://t.me/Smudgejasmine313")

time.sleep(1)

elem=driver.find_element(By.ID ,"phone_number")
elem.send_keys("09019982149")

time.sleep(1)


elem=driver.find_element(By.ID ,"password")
elem.send_keys("12911294karim")

time.sleep(1)

elem=driver.find_element(By.ID ,"password_confirmation")
elem.send_keys("12911294karim")

time.sleep(1)

elem=driver.find_element(By.CSS_SELECTOR,"form > div:nth-child(15) > label > input")
elem.click()


# eleme = WebDriverWait(driver, 50)
# elem.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/form/button"))).click()


time.sleep(5)
elem=driver.find_element(By.CSS_SELECTOR,"form button")
print(elem)
elem.click()

# elem.sebd_keys(Keys.RETURN)