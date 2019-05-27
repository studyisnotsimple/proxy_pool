from storage_module import RedisClient
from random import choice
import requests

VALID_STATUS_CODE = [200]
# 此处修改为你需要爬取的网页，这里以58同城里的一个链接为例
TEST_URLS = ['https://cq.58.com/banan/ershoufang/?PGTID=0d30000c-0002-5b08-ae5b-170252d96666&ClickID=1']

class Tester(object):
    def __init__(self):
        self.redis = RedisClient()  #初始化，连接redis

    def test_single_proxy(self, proxy):
        TEST_URL = choice(TEST_URLS)
        # 这里针对你要爬的网站，修改headers内容
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        }

        try:
            real_proxy = {
                'https': '{}'.format(proxy)
            }
            print('正在测试', proxy)
            response = requests.get(TEST_URL, proxies=real_proxy, timeout=7, headers=headers)
            if response.status_code in VALID_STATUS_CODE:
                self.redis.max(proxy)
                print('代理可用', proxy)

            else:
                self.redis.decrease(proxy)
                print('非高匿代理', proxy)  # 返回重定向，人机验证非200的status_code，代理隐藏得不深
        # 报错，超时的代理都不能用，一律'请求失败'
        except:
            self.redis.decrease(proxy)
            print('代理请求失败')

    def run(self):

        print('测试器开始运行')
        try:
            proxies = self.redis.all()  # 获取当前代理池列表

            self.test_single_proxy(choice(proxies))  #选择一个进行验证

        except Exception as e:
            print('测试器发生错误', e.args)
