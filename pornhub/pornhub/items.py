# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PornhubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag = scrapy.Field()                        # 分类属性
    duration = scrapy.Field()                   # 时长
    title = scrapy.Field()                      # 标题
    link_url = scrapy.Field()                   # 详情页url
    count = scrapy.Field()                      # 观看次数
    video_tags = scrapy.Field()                 # 视频属性
    percent = scrapy.Field()                    # 好评率
    img_url = scrapy.Field()                    # 视频封面
    video_screenshot_imgs = scrapy.Field()      # 视频截图
    video_url = scrapy.Field()                  # 视频url



