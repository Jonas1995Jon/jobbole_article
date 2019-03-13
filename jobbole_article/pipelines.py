# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

import pymongo
from jobbole_article.settings import mongo_host, mongo_port, mongo_db_name, mongo_db_collection

class JobboleArticlePipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        db_name = mongo_db_name
        sheet_name = mongo_db_collection
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[db_name]
        self.post = mydb[sheet_name]
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

class JsonWithEncoding(object):
    def __init__(self):
        self.file = codecs.open('jobbole_article.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        lines = json.dumps(item, ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item
    def spider_closed(self):
        self.file.close()