# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import pymongo
from pornhub.items import PornhubItem
from pornhub.settings import *

class PornhubPipeline(object):

    def __init__(self):
        # host = MONGODB_HOST
        # post = MONGODB_POST
        name = BOT_NAME

        self.client = pymongo.MongoClient()
        self.db = self.client[name]

        # 用来计数的
        self.count = 1

    def process_item(self, item, spider):

        if isinstance(item,PornhubItem):
            try:
                self.db[item['tag']].insert(dict(item))
                print('保存成功',self.count,  item['link_url'])

            except:
                print('monogdb 保存失败',  item['link_url'])
                with open('erorr_save.txt', 'a')as f:
                    f.write(str(item))
                    f.write('\n')

        self.count += 1
        return item

    def close_spider(self, spider):
        self.client.close()
