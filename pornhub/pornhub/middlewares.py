# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import user_agent
import requests

class Pornhub_UA_Middleware(object):
    def process_request(self,request,spider):
        request.headers['User_Agent'] = user_agent.generate_user_agent()


# 没有国外ip GG 只能用vpn的固定ip  如果有请随机ip
# 更新 貌似是因为小水管的问题,我也就1秒一个多左右的请求,没封ip .不过最好还是隔半天换一个ip
class Pornhub_IP_Middleware(object):

    def __init__(self):
        self.ip_url = 'http://188.131.212.24:5010/get/'
        self.ip = ''
        self.ip_count = 0

    def process_request(self,request,spider):
        if self.ip_count == 0 or self.ip_count == 10:
            res = requests.get(self.ip_url).content.decode()
            if not 'no proxy!' in res:
                self.ip = res
            self.ip_count = 1
        request.meta['proxy'] = 'http://' + self.ip
        self.ip_count += 1
        print('ip地址>>>',self.ip)


    def process_exception(self, request, exception, spider):
        if isinstance(exception, TimeoutError):
            return request

