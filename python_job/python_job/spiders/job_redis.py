# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

from python_job.items import PythonJobItem


class JobSpider2(RedisSpider):
    name = 'job2'
    allowed_domains = ['51job.com','search.51job.com']
    # 添加起始路径的时候：lpush  myspider:start_urls 起始路径
    redis_key = 'jobspider2:start_urls'
    # page = 1
	 #
    # pre = 'https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,'
	 #
    # suf = '.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
	 #
	 #
    # start_urls = [pre+str(page)+suf]

    def parse_detail(self,response):

        item = PythonJobItem()
        print("response.url==", response.url)
        title = response.xpath('//div[@class="cn"]/h1/text()').extract()
        title = "".join(title)

        location = response.xpath('//div[@class="cn"]/span/text()').extract()
        location = "".join(location)

        salary = response.xpath('//div[@class="cn"]/strong/text()').extract()

        salary = "".join(salary)

        company_name = response.xpath('//div[@class="cn"]/p/a/text()').extract()
        company_name = "".join(company_name)

        company_info = response.xpath('//div[@class="cn"]/p[@class="msg ltype"]/text()').extract()
        company_info = "".join(company_info)

        experience = response.xpath('//div[@class="t1"]/span[1]/text()').extract()
        experience = "".join(experience)

        job_info = response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()|//div[@class="bmsg job_msg inbox"]/text()|//div[@class="bmsg job_msg inbox"]//p//span/text()').extract()
        job_info = "".join(job_info)

        address = response.xpath('//div[@class="bmsg inbox"]/p/text()').extract()

        address = "".join(address)
        item["url"] = response.url

        item["title"] = title
        item["location"] = location

        item["salary"] = salary

        item["company_name"] = company_name

        item["company_info"] = company_info

        item["experience"] = experience

        item["job_info"] = job_info

        item["address"] = address
        # print(item)
        yield  item





        # print("title==",title)
		  #
        # print("location==", location)
		  #
        # print("salary==", salary)
		  #
        # print("company_name==", company_name)
		  #
        # print("company_info==", company_info)
        # print("experience==", experience)
        # print("job_info==", job_info)
		  #
        # print("address==", address)


    def parse(self, response):
        # print("response.url==",response.url)
        links = response.xpath('//div[@class="el"]/p//a/@href').extract()

        for link in links:
            yield scrapy.Request(link,callback=self.parse_detail)


        #得到下一页案例是否还有链接
        next_url = response.xpath('//li[@class="bk"][last()]/a/@href').extract()
        if next_url:
            url = next_url[0]
            yield scrapy.Request(url,self.parse)
        else:
            print('所有的页都已经抓取')

