from flask import Flask, g
from storage_module import RedisClient

__all__ = ['app']
app = Flask(__name__)
app.config['DEBUG'] = True  #debug模式开启

def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')  #主页
def index():
    return "this is my proxy_pool"

@app.route('/random')  #从代理池中随机抽取一个代理
def get_proxy():
    conn = get_conn()
    return conn.random()

@app.route('/count')  #对代理池中代理个数进行统计
def get_counts():

    conn = get_conn()
    return str(conn.count())

if __name__ == '__main__':
    app.run()
