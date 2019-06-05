# -*- coding: utf-8 -*-
import scrapy
import re
from pornhub.items import PornhubItem
from scrapy_redis.spiders import RedisSpider


class PhbSpider(scrapy.Spider):
    name = 'phb'
    allowed_domains = ['pornhub.com']
    start_urls = ['https://www.pornhub.com/categories?o=al']

# 分布式
# class PhbSpider(RedisSpider):
#     name = 'phb'
#     allowed_domains = ['pornhub.com']
#     # start_urls = ['https://www.pornhub.com/categories?o=al']
#     redis_key = 'start_urls:phb'

    # 所有104个分类 属性
    def parse(self, response):

        lis = response.xpath('//ul[@id="categoriesListSection"]/li')
        for li in lis:
            href = response.urljoin(li.xpath('./div/h5/a/@href').get())
            tag = li.xpath('./div/h5/a/strong/text()').get()

            yield scrapy.Request(url=href,
                                 callback=self.parse_video,
                                 meta={'item':tag})



    def parse_video(self,response):

        tag = response.meta.get('item')

        # 第一个是广告,剔除
        lis = response.xpath('//ul[@id="videoCategory"]/li')[1:]
        for li in lis:
            duration = li.xpath('./div//var[@class="duration"]/text()').get()
            href = response.urljoin(li.xpath('.//span[@class="title"]/a/@href').get())

            yield scrapy.Request(url=href,
                                 callback=self.video_content,
                                 meta={'item':(tag,duration)})

        # 下一页
        next_url = response.urljoin(response.xpath('//li[@class="page_next"]/a/@href').get())
        if next_url:
            yield scrapy.Request(url=next_url,
                                 callback=self.parse_video,
                                 meta={'item': tag})



    def video_content(self,response):
        tag,duration = response.meta.get('item')

        item = PornhubItem()

        link_url = response.url

        try:
            title = response.xpath('//span[@class="inlineFree"]/text()').get()
        except:
            title = None

        try:
            count = response.xpath('//span[@class="count"]/text()').get()
        except:
            count = None

        try:
            video_tags = ','.join(response.xpath('//div[@class="categoriesWrapper"]/a//text()').getall())
        except:
            video_tags = None

        try:
            percent = response.xpath('//span[@class="percent"]/text()').get()
        except:
            percent = None

        try:
            img_url = response.xpath('//meta[@property="og:image"]/@content').get()
        except:
            img_url = None




        # 得到视频截图,其中S{?} 代表有多少个视频截图,得到值,将img切割,推导式拼接
        # 有一定情况出现问题
        try:
            video_screenshot_img = re.findall('"urlPattern":"(.*?)","thumbHeig',response.text)[0]
            num = int(re.findall('S{(\d+)}',video_screenshot_img)[0])
            start_video_img = video_screenshot_img.split('S{')[0]
            video_screenshot_imgs = [start_video_img+'S{}.jpg'.format(i) for i in range(1,num)]
        except:
            video_screenshot_imgs = None


        # 有一定情况出现问题
        # 网络小水管,1080p是必须登陆才能在页面上看到的,如果需要请携带cookies重写中间件
        # 如果需要下载视频,请携带请求头请求,不然返回403
        # if '"quality":"1080"' in response.text:
        #     video_url = re.findall('"quality":"1080","videoUrl":"(.*?)"},',response.text,re.S|re.I)[0]
        try:
            if '"quality":"720"' in response.text:
                video_url = re.findall('"quality":"720","videoUrl":"(.*?)"},', response.text, re.S | re.I)[0]
            elif '"quality":"480"' in response.text:
                video_url = re.findall('"quality":"480","videoUrl":"(.*?)"},', response.text, re.S | re.I)[0]
            elif '"quality":"240"' in response.text:
                video_url = re.findall('"quality":"240","videoUrl":"(.*?)"},', response.text, re.S | re.I)[0]
        except:
            video_url = None
            with open('erorr_request.txt','a')as f:
                f.write(title+','+link_url)
                f.write('\n')

        item['tag'] = tag
        item['duration'] = duration
        item['title'] = title
        item['link_url'] = link_url
        item['count'] = count
        item['video_tags'] = video_tags
        item['percent'] = percent
        item['img_url'] = img_url
        item['video_screenshot_imgs'] = video_screenshot_imgs
        item['video_url'] = video_url

        yield item

