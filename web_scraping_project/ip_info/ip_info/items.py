# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def newline(value):
    return value.replace('<br>','\n')

class IpInfoItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field(input_processor = MapCompose(newline, remove_tags), output_processor = TakeFirst())
