# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_verb(value):
    return value.replace('v.','').strip()

def remove_noun(value):
    return value.replace('n.','').strip()

def remove_expression(value):
    return value.replace('expr.','').strip()

def remove_newline(value):
    return value.replace('\r\n','').strip()

class TurengItem(scrapy.Item):
    # define the fields for your item here like:
    word = scrapy.Field(input_processor = MapCompose(remove_tags, remove_verb, remove_noun, remove_expression, remove_newline), output_processor = TakeFirst())
    resp = scrapy.Field(input_processor = MapCompose(remove_tags), output_processor = TakeFirst())
