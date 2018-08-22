import redis
import json
import pymongo

redis_client = redis.StrictRedis(host='192.168.28.23', port=6379,
                 db=0)


mongodb_client = pymongo.MongoClient(host='192.168.28.23',
            port=27017,)

#数据库
dbname = mongodb_client["sina"]

items = dbname["items"]

i = 1

while True:
	print("i===",i)
	#先进先出，先请求的数据，被优先取出
	source,data = redis_client.blpop(["sinainfospider_redis:items"])

	pyton_dict = json.loads(data.decode())
	print("source===",source)
	print("pyton_dict===", pyton_dict)
	items.insert_one(pyton_dict)
	i += 1