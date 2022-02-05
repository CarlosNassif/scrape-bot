# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 18:00:27 2022

@author: Carlos

This challenge is about scraping info of https://sdsclub.com/
From this page, we must go to the Learning Paths page and then select a path to
get information about.
Info to get:
    - Path Meta
    - Market Opportunity
    - Career Opportunity
    - Instructors list
"""

import time
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('C:\Windows\chromedriver\chromedriver.exe')

def scrape(url):
    # go to the root page    
    driver.get(url)
    driver.maximize_window()
    # wait the page to load
    time.sleep(5)
    # go to the second the page    
    driver.find_element_by_xpath('/html/body/header/div/div/div[2]/nav/ul/li[1]/a').click()
    # wait the page to load
    time.sleep(5)
    # go to the third the page   
    driver.find_element_by_xpath('/html/body/section[2]/div/div[2]/div[4]/div/figure/a').click()
    time.sleep(5)
    
    info = []
    
    elements = driver.find_elements_by_xpath('//*[@class="path-meta-item"]')    
    path_meta = []
    for element in elements:
        path_meta.append(element.find_element_by_tag_name('span').text)
    info.append(path_meta)
    
    elements = driver.find_elements_by_xpath('//*[@class="single-path-article"]')
    for i in range(2):
        title = elements[i].find_element_by_tag_name('header').find_element_by_tag_name('h3').text
        about_element = elements[i].find_element_by_tag_name('div').find_element_by_tag_name('p').text
        info.append([title, about_element])

    instructors = driver.find_elements_by_xpath('//*[@class="vcard"]')
    for instructor in instructors:
        info.append(['instructor', instructor.find_element_by_class_name('name').text, instructor.find_element_by_class_name('position').text])
    
    df = pd.DataFrame(info)
    filename = str(time.time())
    df.to_csv(filename + '- file urls.csv')
        
    
scrape('https://sdsclub.com/')
# time to see the page
time.sleep(20)


driver.close()
driver.quit()