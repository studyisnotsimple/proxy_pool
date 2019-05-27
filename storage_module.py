import redis
from random import choice
from error import PoolEmptyError

MAX_SCORE = 100  # 设置keys的分数：最高100分，最低0分，初始分10分
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'  # 配置REDIS
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies_haha'

'''检测规则:获取代理池全部代理列表，从中随机选取一个检测。新加入的代理设置为初始分数。代理检测成功，代理分数设置最高分；
检测失败，代理分数减2。当代理分数小于0或者分数在区间(15,88]时，都判定代理失效，从redis删除。
'''

class RedisClient(object):

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):

        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        if not self.db.zscore(REDIS_KEY, proxy):  # 返回有序集REDIS_KEY中元素proxy对应的分数值，若有序集不存在或有序集中没有这个元素，则返回空
            return self.db.zadd(REDIS_KEY, score, proxy)  # 更新有序集中成员元素的分数值，返回被成功添加的新成员数量

    def random(self):
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)  # 有序集中按score递增排序，在闭区间[MAX_SCORE,MAX_SORE]中的成员列表
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 10)  # reverse递减排序,取前10个
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

    def decrease(self, proxy):
        score = self.db.zscore(REDIS_KEY, proxy)
        if 15 < score <= 88:
            return self.db.zrem(REDIS_KEY, proxy)
        else:
            if score and (score-2) >= MIN_SCORE:
                print('代理', proxy, '当前分数', score, '减2')
                return self.db.zincrby(REDIS_KEY, proxy, -2)  # 给分数加，若此元素不在有序集合内，则add该分数的成员元素,返回新的分数值
            else:
                print('代理', proxy, '当前分数', '移除')
                return self.db.zrem(REDIS_KEY, proxy)  # 移除成员元素，返回被成功移除的成员数量

    def exists(self, proxy):
        return not self.db.zscore(REDIS_KEY, proxy) == None  # 判断这个proxy是否存在，存在返回true

    def max(self, proxy):

        print('代理', proxy, '可用，设置为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        return self.db.zcard(REDIS_KEY)  # 返回存在的有序集的基数

    def all(self):
        # 返回全部代理
        return self.db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)


