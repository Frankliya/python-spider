# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    def process_item(self, item, spider):
        return item


class TenPipeline(object):
    def open_spider(self,spider):
        print('打开文件流===========')
        # self.file = open("tencent.json","w",encoding="utf-8")
        self.file = open("tencent.csv", "w")


    def process_item(self,item,spider):
        print('正在保存数据==============')
        item_dict = dict(item)
        jsontext = json.dumps(item_dict,ensure_ascii=False)+"\n"
        self.file.write(jsontext)
        return item


    def close_spider(self,spider):
        print('关闭文件流=========')
        self.file.close()

