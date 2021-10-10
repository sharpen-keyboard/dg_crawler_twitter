# encoding: utf-8

"""
Scrapy默认中间件
{
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
}
"""

# 日志等级，默认INFO就可
LOG_DEFAULT_LEVEL = "INFO"

# 以下四个为各类插件，可以根据自己需求删除或添加用于测试
BASE_EXTENSIONS = {}

BASE_DOWNLOADER_MIDDLEWARES = {
    'crawler.middlewares.proxy_download_middleware.ProxyDownloaderMiddleware': 544,
    'crawler.middlewares.reply_token_download_middleware.ReplyTokenDownloaderMiddleware': 551,
}

BASE_ITEM_PIPELINES = {}

BASE_SPIDER_MIDDLEWARES = {
    'crawler.middlewares.spider_middleware.SpiderMiddleware': 543,
}