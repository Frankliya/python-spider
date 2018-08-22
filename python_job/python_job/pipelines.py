# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from pymongo import MongoClient
from pymysql import Connect
from python_job.settings import MONGODB_DBNAME,MONGODB_HOST,MONGODB_PORT,SHEETE_NAME
from python_job.settings import MYSQL_DBNAME,MYSQL_HOST,MYSQL_PORT,TABLE_NAME,MYSQL_USER,MYSQL_PASSWORD
class ExamplePipeline(object):
    def process_item(self, item, spider):
        #当前爬取的时间
        item["crawled"] = datetime.utcnow()
        #爬虫的名称
        item["spider"] = spider.name+"_atguigu"
        return item


class PythonJobMongodbPipeline(object):

    def open_spider(self,spider):
        print("爬虫开始了------------------------------------------")
        client = MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)

        dbname = client[MONGODB_DBNAME]
        #集合
        self.conllection = dbname[SHEETE_NAME]


    def process_item(self, item, spider):
        python_dict = dict(item)
        #字典
        self.conllection.insert_one(python_dict)
        return item


class PythonJobMySqlPipeline(object):

    def open_spider(self,spider):
        print("爬虫开始了mysql------------------------------------------")
        self.client = Connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD,
                 database=MYSQL_DBNAME, port=MYSQL_PORT,charset='utf8')

        self.sursor = self.client.cursor()
    def close_spider(self,spider):
        #关闭数据库，释放资源
        self.sursor.close()
        self.client.close()




    def process_item(self, item, spider):
        s = dict(item)

        parms = [s["url"],s["title"],s["location"],s["company_name"],s["salary"],s["company_info"],s["experience"],s["job_info"],s["address"],s["crawled"],s["spider"],]

        sql = "INSERT INTO job_items(url,title,location,company_name,salary,company_info,experience,job_info,address,crawled,spider) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        self.sursor.execute(sql,parms)

        #事务提交
        self.client.commit()

        #字典
        return item


