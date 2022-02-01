# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:17:17 2022

@author: Carlos
"""

import scrapy

from practicalone.items import PracticaloneItem

class SecondSpyder(scrapy.Spider):
    name = "Books2"
    start_urls = [
        "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",
    ]
    
    def parse(self, response):
        item = PracticaloneItem()
        # item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').extract()
        # item['price'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').extract() 
        item['price'] = response.css('.price_color').xpath('text()').get()
        
        return item