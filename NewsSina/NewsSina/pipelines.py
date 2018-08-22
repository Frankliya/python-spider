# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class NewssinaPipeline(object):
    def open_spider(self, spider):
        self.file = open(spider.name + ".json", "w", encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        print("item====", item)
        sub_file_name = item["sub_file_name"]
        print("sub_file_name==", sub_file_name)

        content = item["content"]

        if len(content) > 0:

            file_name = item["son_url"]

            file_name = file_name[7:file_name.rfind(".")].replace("/", "_")

            file_path = sub_file_name + "/" + file_name + ".txt"

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            item["son_path"] = file_path

        python_str = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(python_str)

        return item
