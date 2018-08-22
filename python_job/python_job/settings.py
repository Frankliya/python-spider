# -*- coding: utf-8 -*-

# Scrapy settings for python_job project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'python_job'

SPIDER_MODULES = ['python_job.spiders']
NEWSPIDER_MODULE = 'python_job.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'python_job (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 模拟浏览器身份
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

# 使用scrapy_redis自己的去重处理器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy_redis自己调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 爬虫可以暂停/开始， 从爬过的位置接着爬取
SCHEDULER_PERSIST = True

# 不设置的话，默认使用的是SpiderPriorityQueue

# 优先级队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 普通队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
	# scrapy默认配置
	'python_job.pipelines.ExamplePipeline': 300,
	'python_job.pipelines.PythonJobMongodbPipeline': 301,
	'python_job.pipelines.PythonJobMySqlPipeline': 302,

	# 把数据默认添加到redis数据库中
	'scrapy_redis.pipelines.RedisPipeline': 400,

}

# 日志基本
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
# 下载延迟1秒
# DOWNLOAD_DELAY = 1


# 配置redis数据库信息

# redis数据库主机---
REDIS_HOST = "192.168.28.23"
# redis端口
REDIS_PORT = 6379

# 配置mongodb相关配置
MONGODB_HOST = "192.168.28.23"
MONGODB_PORT = 27017

# 数据库名称
MONGODB_DBNAME = "JOB"
SHEETE_NAME = "job_item"


#mysql配置
MYSQL_HOST = "192.168.28.23"
MYSQL_PORT = 3306

MYSQL_DBNAME = "job"
TABLE_NAME = "job_items"

MYSQL_USER = "afu"
MYSQL_PASSWORD = "123456"


#配置动态浏览器头
#浏览器user-agent列表,USER_AGENTS名字可以任意
USER_AGENTS = [
'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
]


DOWNLOADER_MIDDLEWARES = {
   # 'douban.middlewares.DoubanDownloaderMiddleware': 543,
   'python_job.middlewares.RandomUserAgent': 543,
}

