# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 19:39:32 2022

@author: Carlos

Challenge Scenery:
    - Cybersecurity analyst at COMPANY_X
    - COMPANY_X has a lot of sensitive information
    - COMPANY_X is target frequently by hackers
    - We must to be sure about any info leaked
        - externally
        - internally
            - someone posting code or sharing code with sensitive information

Challenge URL:
    - "https://pastebin.com/Mfc9txQV"
    
We must create an alert based on searching the page for the word "key".
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

driver = webdriver.Chrome('C:\Windows\chromedriver\chromedriver.exe')


# open the URL
driver.get("https://pastebin.com/Mfc9txQV")
time.sleep(5)

# get page structure
soup = BeautifulSoup(driver.page_source, 'lxml')

# find all 'key' strings on page body
key_strings = soup.find('body').find_all(string=re.compile('(?i)key'))

if len(key_strings) > 0:
    print("KEY LEAKED!!!")
else:
    print("We couldn't find any 'key'")

time.sleep(10)

driver.quit()