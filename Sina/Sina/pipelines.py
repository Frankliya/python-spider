# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import json

class ExamplePipeline(object):
    def process_item(self, item, spider):
        #当前爬取的时间
        item["crawled"] = datetime.utcnow()
        #爬虫的名称
        item["spider"] = spider.name+"_atguigu"
        return item


class SinaPipeline(object):
    def open_spider(self,spider):
        self.file = open(spider.name+".json","w",encoding="utf-8")

    def close_spider(self,spider):
        self.file.close()
    def process_item(self, item, spider):
        print("item====",item)
        sub_file_name = item["sub_file_name"]
        print("sub_file_name==",sub_file_name)

        content = item["content"]

        if len(content) > 0:

            #'http://news.sina.com.cn/c/sd/2018-01-25/doc-ifyqyuhy6201774.sss.shtml',
            #

            file_name = item["son_url"]
            #切片，从右边查找，替换
            file_name = file_name[7:file_name.rfind(".")].replace("/","_")

            #'./Data/新闻/国内',
            # './Data/新闻/国内/lslsllll.txt',
            file_path = sub_file_name+"/"+file_name+".txt"

            with open(file_path,"w",encoding="utf-8") as f:
                f.write(content)

            item["son_path"] =file_path



        # python_str = json.dumps(dict(item),ensure_ascii=False)+"\n"
        # self.file.write(python_str)


        return item
