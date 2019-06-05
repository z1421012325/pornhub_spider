# -*- coding: utf-8 -*-



BOT_NAME = 'pornhub'
SPIDER_MODULES = ['pornhub.spiders']
NEWSPIDER_MODULE = 'pornhub.spiders'

ROBOTSTXT_OBEY = False
# log输出等级
LOG_LEVEL = 'WARNING'
# 爬虫运行多久关闭
# CLOSESPIDER_TIMEOUT = 86400   # 24小时*3600秒 = 86400
# DOWNLOAD_DELAY = 2
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}
DOWNLOADER_MIDDLEWARES = {
   'pornhub.middlewares.Pornhub_UA_Middleware': 543,
}
ITEM_PIPELINES = {
   'pornhub.pipelines.PornhubPipeline': 300,
}




MONGODB_HOST = '127.0.0.1'
MONGODB_POST = 27017

#使用Scrapy-Redis的调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# # 利用Redis的集合实现去重
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# # 允许继续爬取
# SCHEDULER_PERSIST = True
# # 设置优先级
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

# REDIS_HOST = 'redis的host'
# REDIS_POST = 6379
