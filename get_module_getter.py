from storage_module import RedisClient

from get_module_crawl import Crawler

POOL_UPPER_THRESHOLD = 20  # 设定当代理池内代理数低于定值20时，开始抓取新代理

class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):

        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False
    def run(self):
        if not self.is_over_threshold():
                print('获取代理开始')
                callback = self.crawler.crawl_xiladaili
                proxies = self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)



