import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import pandas as pd
from collections import defaultdict, namedtuple

# full path to the webdriver to use; use webdriver.PhantomJS() for invisible browsing
driver = webdriver.Chrome('/Users/ik/Codes/hotel-emails-tripadvisor/webdriver/chromedriver')
# default waiting time
WAIT_TIME = 40
# page to go to first
start_page  = "https://www.commbank.com.au/digital/locate-us/"
driver.get(start_page)
time.sleep(5)
# find the "Select a Service" dropdown menu
service_ddmenu = Select(driver.find_element_by_id("searchTypeSelect"))
print([o.text for o in service_ddmenu.options])
service_ddmenu.select_by_visible_text("ATM")
time.sleep(3)
search_field = driver.find_element_by_id("addressSearch")
search_field.send_keys("NSW, Australia")
# find the Search button
driver.find_element_by_id("submitButtonLanding").click()
time.sleep(10)
driver.quit()