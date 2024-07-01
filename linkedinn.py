from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

# Create Chromeoptions instance 
options = webdriver.ChromeOptions() 
 
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
 
# Setting the driver path and requesting a page 
driver = webdriver.Chrome(options=options) 
 
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")




driver = webdriver.Chrome() 
 
# Initializing a list with two Useragents 
useragentarray = [ 
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", 
] 

for i in range(len(useragentarray)): 
  # Setting user agent iteratively as Chrome 108 and 107 
  driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]}) 
  print(driver.execute_script("return navigator.userAgent;")) 
  driver.get("https://www.httpbin.org/headers") 
  
driver.close()




options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)#, executable_path=r"C:\Users\Fatemeh\Desktop\chromedriver-win64\chromedriver-win64")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )




# url = "https://api.linkedin.com/login"
# driver.get(url)
# time.sleep(5)
# # driver.quit()

driver.get("https://api.linkedin.com/login")
time.sleep(2)


elem=driver.find_element(By.ID,"username")
elem.send_keys("f.karimshahi.86@gmail.com")
time.sleep(2)

time.sleep(4.10) 
driver.execute_script('window.scrollTo(0, 700)') 


elem=driver.find_element(By.ID , "password")
elem.send_keys("1250903785karim")

time.sleep(4.10) 
driver.execute_script('window.scrollTo(0, 700)') 

elem=driver.find_element(By.CSS_SELECTOR, " form > div.login__form_action_container > button").click()
time.sleep(5)

