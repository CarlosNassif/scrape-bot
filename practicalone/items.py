# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PracticaloneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    title = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()
    stock_availability = scrapy.Field()
    
    pass
