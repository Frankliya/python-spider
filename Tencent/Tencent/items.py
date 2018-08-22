# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cot_name = scrapy.Field()
    cot_link = scrapy.Field()
    cot_type = scrapy.Field()
    cot_num = scrapy.Field()
    cot_add = scrapy.Field()
    cot_time = scrapy.Field()
