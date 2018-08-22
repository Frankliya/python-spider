# -*- coding: utf-8 -*-
import scrapy,os
from NewsSina.items import NewssinaItem


class NewsinaSpider(scrapy.Spider):
    name = 'Newsina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse_detail(self,response):
        item = response.meta["item"]

        item["son_url"] = response.url
        heads = response.xpath('//h1[@class="main-title"]/text()|//div[@class="blkContainerSblk"]/h1[@id="artibodyTitle"]/text()').extract()
        head = "".join(heads).strip()

        contents = response.xpath('//div[@class="article"]/p/text()|//div[@id="artibody"]/p/text').extract()
        content = "".join(contents).strip()

        item["head"] = head
        item["content"] = content

        yield item


    def parse_second(self,response):
        son_urls = response.xpath('//a/@href').extract()
        item = response.meta["item"]
        parent_url = item["parent_url"]
        for url in son_urls:
            if url.startswith(parent_url) and url.endswith(".shtml"):
                yield scrapy.Request(url,callback=self.parse_detail,meta={"item":item})


    def parse(self, response):
        parent_titles = response.xpath('//h3[@class="tit02"]/a/text()').extract()
        parent_urls = response.xpath('//h3[@class="tit02"]/a/@href').extract()

        sub_titles = response.xpath('//ul[@class="list01"]/li/a/text()').extract()
        sub_urls = response.xpath('//ul[@class="list01"]/li/a/@href').extract()

        items = []

        for i in range(len(parent_urls)):
            parent_url = parent_urls[i]
            parent_title = parent_titles[i]

            for j in range(len(sub_urls)):
                sub_url = sub_urls[j]
                sub_title = sub_titles[j]

                if sub_url.startswith(parent_url):
                    item = NewssinaItem()

                    sub_file_name = "./Data/"+parent_title+"/"+sub_title
                    if not os.path.exists(sub_file_name):
                        os.makedirs(sub_file_name)

                    item["parent_url"] = parent_url
                    item["parent_title"] = parent_title
                    item["sub_url"] = sub_url
                    item["sub_title"] = sub_title
                    item["sub_file_name"] = sub_file_name

                    items.append(item)
        for item in items:
            sub_url = item["sub_url"]
            yield scrapy.Request(sub_url,callback=self.parse_second,meta={"item":item})


