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
atm_list = []
ATM = namedtuple("ATM", "logo name address")
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
lis = driver.find_elements_by_xpath("//li[@id='detailViewListAtm']")
print("see {} list items".format(len(lis)))
time.sleep(5)
for item in lis[:10]:
	logotype = item.find_element_by_xpath(".//div/div[contains(@class,'ico-')]").get_attribute("class")
	print("logo: {}".format(logotype))
	name = item.find_element_by_xpath(".//div/h3").text.lower()
	print("name: {}".format(name.lower()))
	__ = []
	address_lines = item.find_elements_by_xpath(".//div[contains(@data-ng-bind, 'location')]")
	for l in address_lines[:-1]:
		__.append(l.text.lower())
	addr = " ".join(__).strip()
	print("address: {}".format(addr))
	atm_list.append(ATM(logo=logotype, name=name, address=addr))
# now need to do another search via the Modify search button
driver.find_element_by_id("modifySearchButton").click()
time.sleep(5)
search_field = driver.find_element_by_id("addressSearch")
search_field.send_keys("Sydney")
driver.find_element_by_id("updateButton").click()
time.sleep(10)
driver.quit()
print(atm_list)