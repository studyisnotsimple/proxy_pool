import requests
from lxml import etree

class Crawler(object):

    def get_proxies(self, callback):
        proxies = []
        for proxy in callback():
            print('成功获取到代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_xiladaili(self):

        url_ = 'http://www.xiladaili.com/gaoni/'  # 代理ip网站

        r_ = requests.get(url_).text

        s_ = etree.HTML(r_)

        a_ = s_.xpath('/html/body/div/div[3]/div[2]/table/tbody/tr/td[1]/text()')  # 获取代理ip列表

        a_ = a_[0:20]  # 这里只取列表中的前20个放入代理池

        return a_
