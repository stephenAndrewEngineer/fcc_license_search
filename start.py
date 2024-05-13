#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # keyboard keys
from selenium.webdriver.common.by import By # used to locate elements within a document
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org") # http GET
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q") # find the input text element (<input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">)
elem.clear() # make sure no keys are entered so far
elem.send_keys("pycon") # type in this string
elem.send_keys(Keys.RETURN) # press return to send the form
assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()
