# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 07:45:37 2022

@author: Carlos
"""

import requests
from bs4 import BeautifulSoup

r = requests.get("https://quotes.toscrape.com")

# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)

soup = BeautifulSoup(r.content, 'lxml')

quotes = soup.find_all("div", class_="quote")

for x in quotes:
    quote = x.find('span').text
    print('quote -> ', quote)
    tags = x.find_all("a", class_='tag')
    print('tags:')
    for i in tags:    
        print('\t - ', i.text.strip())