# encoding: utf-8

from scrapy.downloadermiddlewares.retry import RetryMiddleware

class ReplyTokenDownloaderMiddleware:
    '''
    reply下载中间件
    '''
    def process_request(self, request, spider):
        spider.make_header(request)
        spider.token_count += 1
        if spider.token_count > 500:
            spider.get_token()
            spider.token_count = 0
        request.headers['x-guest-token'] = spider.token

    def process_response(self, request, response, spider):
        try:
            if response.status >= 300 or response.status <200:
                spider.get_token()
                spider.send_log(2, "状态码错误 ==> status:{} ==> url:<{}>".format(response.status, response.url))
            return response
        except Exception as e:
            spider.send_log(3, "ReplyDownloaderMiddleware error ==> {} ==> url:<{}>".format(e, response.url))

    def process_exception(self, request, exception, spider):
        if isinstance(exception, RetryMiddleware.EXCEPTIONS_TO_RETRY):
            spider.send_log(3, 'downloader error ==> ({}) ==> url:<{}>'.format(exception, request.url))