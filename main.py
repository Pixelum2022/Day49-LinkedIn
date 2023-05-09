# import modules :
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Init Variables:
mon_email = 'harnais_minimal.0@icloud.com'
mon_mp = '^&JL3wbJMPh8^LkXfovo'
site_url = 'https://www.linkedin.com/home'
chrome_driver_path = "/Applications/chromedriver_mac_arm64/chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(site_url)

