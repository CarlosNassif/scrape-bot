# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:38:53 2022

@author: Carlos

Challange:
    Get four (4) books and return:
        Their price;
        Their title;
        Their category;
        Their stock availability.
"""

import scrapy

from practicalone.items import PracticaloneItem

class ChallangeSpider(scrapy.Spider):
    
    name = "Challange1"
    start_urls = [
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
        "https://books.toscrape.com/catalogue/the-requiem-red_995/index.html",
        "https://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html",
        "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",
    ]
    
    def parse(self, response):
        item = PracticaloneItem()
        
        item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1/text()').get()
        item['price'] = response.css('#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color').xpath('text()').get()
        item['category'] = response.xpath('/html/body/div/div/ul/li[3]/a/text()').get()
        stock_availability = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()').getall()
        text = ""
        for x in stock_availability:
            print('x -> ', x)
            if not(x.isspace()):
                text = x
        item['stock_availability'] = text.strip()
        return item
            
            