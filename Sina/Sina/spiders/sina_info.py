# -*- coding: utf-8 -*-
import scrapy
import os

from scrapy_redis.spiders import RedisSpider

from Sina.items import SinaItem


class SinaInfoSpider(RedisSpider):
    name = 'sina_redis'
    allowed_domains = ['sina.com.cn']
    # 添加起始路径的时候：lpush  myspider:start_urls 起始路径
    redis_key = 'sina:start_urls'

    # start_urls = ['http://news.sina.com.cn/guide/']


    def parse_detail(self,response):
        """解析帖子的数据"""
        item = response.meta["item"]
        #帖子链接
        item["son_url"] = response.url
        print("response.url===",response.url)
        heads = response.xpath('//h1[@class="main-title"]/text()|//div[@class="blkContainerSblk"]/h1[@id="artibodyTitle"]/text()').extract()

        head = "".join(heads)
        #把节点转换成unicode编码
        contents = response.xpath('//div[@class="article"]/p/text()|//div[@id="artibody"]/p/text()').extract()

        content = "".join(contents)

        item["content"] = content
        item["head"] = head
        # print("item=====",item)
        yield item




    #解析第二层的方法
    def parse_second(self,response):
        #得到帖子的链接
        # print("parse_second--response.url====", response.url)
        son_urls = response.xpath('//a/@href').extract()
        item = response.meta["item"]
        parent_url = item["parent_url"]

        print(item)

        # print("item====",item)
        for url in son_urls:
            #判断当前的页面的链接是否属于对应的类别
           if url.startswith(parent_url) and url.endswith(".shtml"):
               #请求
               yield scrapy.Request(url, callback=self.parse_detail, meta={"item": item},dont_filter=False)




    def parse(self, response):
        # print("response.url====",response.url)
        #所以的大标题
        parent_titles = response.xpath('//h3[@class="tit02"]/a/text()').extract()
        # 大标题对应的所以的链接
        parent_urls = response.xpath('//h3[@class="tit02"]/a/@href').extract()

        #所有小标题
        sub_titles = response.xpath('//ul[@class="list01"]/li/a/text()').extract()
        #所以小标题对应的链接
        sub_urls = response.xpath('//ul[@class="list01"]/li/a/@href').extract()

        # print(sub_titles)

        items = []

        for i in range(len(parent_titles)):

            #http://news.sina.com.cn/ 新闻
            parent_url = parent_urls[i]

            parent_title = parent_titles[i]

            for j in range(len(sub_urls)):
                #http://news.sina.com.cn/world/  国际
                sub_url = sub_urls[j]
                sub_title = sub_titles[j]

                #判断url前缀是否相同，相同就是属于，否则不属于
                if sub_url.startswith(parent_url):
                    #装数据
                    item = SinaItem()
                    # print("parent_url===",parent_url)
                    # print("sub_url===", sub_url)
                    #创建目录
                    sub_file_name = "./Data/"+parent_title+"/"+sub_title
                    if  not os.path.exists(sub_file_name):
                        #不存在就创建
                        os.makedirs(sub_file_name)

                    item["parent_url"] = parent_url
                    item["parent_title"] = parent_title
                    item["sub_url"] = sub_url
                    item["sub_title"] = sub_title
                    item["sub_file_name"] = sub_file_name

                    items.append(item)


        #把列表的数据取出
        for  item in items:
            sub_url = item["sub_url"]
            #meta={"item":item} 传递item引用SinaItem对象
            yield scrapy.Request(sub_url,callback=self.parse_second,meta={"item":item}, dont_filter=False)














