# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TopAlbum(scrapy.Item):
    index = scrapy.Field()
    title = scrapy.Field()
    artist = scrapy.Field()
    year = scrapy.Field()
    label = scrapy.Field()
    description = scrapy.Field()
