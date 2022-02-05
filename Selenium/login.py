# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:26:42 2022

@author: Carlos
"""

# importar selenium pra fazer o webscrape e time para executar delays
from selenium import webdriver
import time

# carregar o driver do chrome
driver = webdriver.Chrome('C:\Windows\chromedriver\chromedriver.exe')

def open_site(url):
    driver.get(url)
    time.sleep(30)
    driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/nav/a[5]').click()
    
    
    
def login_site():
    time.sleep(30)
    driver.find_element_by_name('email').send_keys('meu_email123@gmail.com')
    driver.find_element_by_name('password').send_keys('senha123')
    driver.find_element_by_name('email').submit()
    
    
    
# abrir a url
open_site('https://www.superdatascience.com/')
login_site()
time.sleep(30)

driver.quit()