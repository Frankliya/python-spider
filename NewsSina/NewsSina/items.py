# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewssinaItem(scrapy.Item):
    # 大标题
    parent_title = scrapy.Field()
    # 大标题链接
    parent_url = scrapy.Field()

    # 小标题
    sub_title = scrapy.Field()
    # 小标题链接
    sub_url = scrapy.Field()
    # 大标题和小标题对应的目录
    sub_file_name = scrapy.Field()
    # 内容的链接
    son_url = scrapy.Field()
    # 具体内容的标题
    head = scrapy.Field()
    # 内容
    content = scrapy.Field()
    #保存的路径
    son_path = scrapy.Field()


