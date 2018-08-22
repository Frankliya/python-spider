from scrapy import cmdline

# cmdline.execute(("scrapy crawl tencnet -o tencent.csv").split())

cmdline.execute(("scrapy crawl tencent -o tencent.json").split())