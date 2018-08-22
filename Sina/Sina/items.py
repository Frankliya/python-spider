# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    #大标题
    parent_title = scrapy.Field()
    #大标题对应的链接
    parent_url = scrapy.Field()
    #小标题
    sub_title = scrapy.Field()
    #小标题的链接
    sub_url = scrapy.Field()

    #大标题和小标题对应的目录
    sub_file_name = scrapy.Field()

    #新闻相关内容
    son_url = scrapy.Field()

    #帖子标题
    head = scrapy.Field()
    #帖子的内容
    content = scrapy.Field()
    #帖子最后存储的位置
    son_path = scrapy.Field()

    spider = scrapy.Field()
    crawled = scrapy.Field()



