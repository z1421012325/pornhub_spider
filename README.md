# pornhub_spider
爬取pornhub 上所有视频


一天大概爬取8w多条,出错率低于1%左右(页面问题)





全部分类页面开始进行爬取
https://www.pornhub.com/categories?o=al

其中每个详情页的数据还是很好看到的,视频url是给html和json混合在一起的,使用re可以找到,根据清晰度选择清晰度url

视频截图 还是进行一定混淆,含在json数据中  ...S{数字}.jpg  是含有多少张视频截图图片,得到数字值,将img切割,推导式拼接

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------


ip 我只有免费vpn,还是小水管10K-60K,请求频率也不是很快,一秒一个左右,暂时发现一定程度(6000-15000)会出现ip发现是爬虫

保存在MongoDB中的中的中，以每个分类tag作为一个集合保存每个分类中的视频

如果保存失败 erorr_save.txt 保存其中,等待之后进行重新抓取


抓取过程中如果发现页面中没有视频的url,那么可能是页面格式还是啥的有问题,保存为 erorr_request.txt


本来 img_url ,video_screenshot_imgs ,video_url  有一定该类出现错误,选择 try...except 以免出错影响程序

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------

如果想要分布式,请在settings.py和主程序phb.py中将注释注释掉

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
如果想要下载视频,请请求中携带UA 和 link_url,403警告
