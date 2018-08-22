# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PythonJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # url（职位的连接）
    url = scrapy.Field()
    # title（招聘标题）
    title = scrapy.Field()
    # location（地点）
    location = scrapy.Field()
    # company_name （公司名称）
    company_name = scrapy.Field()
    # salary（薪水）
    salary = scrapy.Field()
    # company_info(公司信息)
    company_info = scrapy.Field()
    # experience(工作经验)
    experience = scrapy.Field()
    # job_info（职位信息）
    job_info = scrapy.Field()
    # address(联系方式)
    address = scrapy.Field()
    crawled = scrapy.Field()
    spider = scrapy.Field()
