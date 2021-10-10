# encoding: utf-8

from config.host_config import *

class ProxyDownloaderMiddleware:
    '''
    proxy下载中间件
    '''

    def process_request(self, request, spider): 
        try:
            request.meta['proxy'] = PROXY_HOST_LIST['01']
        except Exception as e:
            spider.send_log(3, "ProxyDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, request.url))