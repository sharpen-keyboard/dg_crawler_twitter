# encoding: utf-8

import scrapy


class AckItem(scrapy.Item):
    res = scrapy.Field()

class TweetItem(scrapy.Item):
    id = scrapy.Field() # tweet id
    url = scrapy.Field() # tweet url
    q = scrapy.Field() # 高级搜索匹配字符串
    content = scrapy.Field() # tweet正文
    uname = scrapy.Field() # 用户id
    pub_time = scrapy.Field() # 发布时间
    retweet_count = scrapy.Field() # 转载数
    favorite_count = scrapy.Field() # 喜欢数
    reply_count = scrapy.Field() # 回复数
    quote_count = scrapy.Field() # 引用数
    replies = scrapy.Field() # 回复tweet列表，成员格式与本item相同
    entities = scrapy.Field() # tweet相关资源，一般存图片url
