# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 08:10:08 2022

@author: Carlos
"""

import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Windows\chromedriver\chromedriver.exe')

driver.get("https://www.google.com")

searchBar = driver.find_element_by_xpath('//*[@class="gLFyf gsfi"]')

estado = "Minas Gerais"

time.sleep(1)
searchBar.send_keys('Coronavirus noticias ' + estado)
time.sleep(1)
searchBar.submit()

time.sleep(10)
driver.quit()

