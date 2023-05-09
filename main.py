# import modules :
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Init Variables:
mon_email = 'harnais_minimal.0@icloud.com'
mon_mp = '^&JL3wbJMPh8^LkXfovo'
site_url = 'https://www.linkedin.com/home'
chrome_driver_path = "/Applications/chromedriver_mac_arm64/chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(site_url)

# find field and enter user name:
my_user_name = driver.find_element(By.ID, 'session_key')
my_user_name.send_keys(mon_email)

# find field and enter password:
my_password = driver.find_element(By.ID, 'session_password')
my_password.send_keys(mon_mp)

# find submit button and click it:
my_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button')
my_button.send_keys(Keys.ENTER)

time.sleep(20)
driver.quit()
# Ok, fonctionne pour se connecter automatiquement sur LinkedIn