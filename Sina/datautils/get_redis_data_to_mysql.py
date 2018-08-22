import redis
import json
import time
from pymysql import connect

redis_client = redis.StrictRedis(host='192.168.28.23', port=6379,
                 db=0)


mysql_client = connect(host="192.168.28.23", user="afu", password="123456",
                 database="sina", port=3306, charset='utf8')

#数据库


cursor = mysql_client.cursor()

i = 1

while True:
	print("i===",i)
	time.sleep(1)
	#先进先出，先请求的数据，被优先取出
	source,data = redis_client.blpop(["sinainfospider_redis:items"])

	item = json.loads(data.decode())
	print("source===",source)
	print("pyton_dict===", item)


	#插入mysql的语句和参数
	sql = "insert into sina_items(parent_url,parent_title,sub_title,sub_url,sub_file_name,son_url,head,content,crawled,spider) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	params = [item["parent_url"],item["parent_title"],item["sub_title"],item["sub_url"],item["sub_file_name"],item["son_url"],item["head"],item["content"],item["crawled"],item["spider"],]

	cursor.execute(sql,params)

	#事务提交
	mysql_client.commit()


	i += 1