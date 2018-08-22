# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    url = "https://hr.tencent.com/position.php?&start="
    st = 10
    start_urls = [url+str(st)+"#a"]

    def parse(self, response):
        cot_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')

        for cot in cot_list:
            item = TencentItem()

            cot_name = cot.xpath('./td[1]/a/text()').extract()[0]
            cot_link = cot.xpath('./td[1]/a/@href').extract()[0]
            cot_type = cot.xpath('./td[2]/text()').get()
            cot_num = cot.xpath('./td[3]/text()').extract()[0]
            cot_add = cot.xpath('./td[4]/text()').extract()[0]
            cot_time = cot.xpath('./td[5]/text()').extract()[0]

            item["cot_name"]=cot_name
            item["cot_link"] = cot_link
            item["cot_type"] = cot_type
            item["cot_num"] = cot_num
            item["cot_add"] = cot_add
            item["cot_time"] = cot_time

            yield item

        # page = response.xpath('//div[@class="left"]/span/text()').get()
        # if self.st < int(page):
        #     self.st += 10

        if self.st < 100:
            self.st += 10

        # 每一页的请求链接
        new_url = self.url + str(self.st)

        yield scrapy.Request(new_url,callback=self.parse)