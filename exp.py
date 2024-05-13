#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # keyboard keys
from selenium.webdriver.common.by import By # used to locate elements within a document
import time

driver = webdriver.Firefox()
driver.get("https://wireless2.fcc.gov/UlsApp/UlsSearch/searchLicense.jsp") # http GET
# go to the geographic search:
elem = driver.find_element(By.LINK_TEXT, "Geographic")
#driver.get(elem.get_attribute('href'))
elem.click()
# find the radio button for 'search by state/county':
elem = driver.find_element(By.NAME,"searchType")
assert elem.get_attribute('value') == 'UGCOUNTY'
elem.click()
# click utah:
elem = driver.find_element(By.NAME,'countyState')
x = elem.find_elements(By.TAG_NAME,'option')
i= [i for i in range(0,len(x)) if x[i].get_attribute('value') == 'UT'][0]
x[i].click()
# select utah county:
elem = driver.find_element(By.NAME,'ulsCounty')
x = elem.find_elements(By.TAG_NAME,'option')
i= [i for i in range(0,len(x)) if x[i].get_attribute('text') == 'UT - Utah'][0]
x[i].click()


submit_button = driver.find_elements(By.TAG_NAME,'input')
submit_button = [i for i in submit_button if i.get_attribute('src').count('newsearch')][0] # there are multiple search buttons, very annoying


"""
#time.sleep(5)
#driver.close()
#https://wireless2.fcc.gov/UlsApp/UlsSearch/searchGeographic.jsp;JSESSIONID_ULSSEARCH=QphzaMPGD2nSNFFCutRJ93O4HJ_eUSE8lHdmuSGRjZ48jJR8TQm5!-762587063!206466490
"""