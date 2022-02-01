# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 08:16:34 2022

@author: Carlos
"""

# section 1 - imports
import scrapy

# section 2 - class with name and start_urls to the scrapy crawl
class FirstSpyder(scrapy.Spider):
    name = "Books"
    start_urls = [
        "https://books.toscrape.com/",
        "https://books.toscrape.com/catalogue/category/books/science_22/index.html",
    ]
    
    # section 3 - will structure the data scraped
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'books-%s.html' % page
        with open(filename, "wb") as f:
            f.write(response.body)