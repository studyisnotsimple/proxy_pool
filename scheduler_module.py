# -*- coding: utf-8 -*-
import time
from api import app
from get_module_getter import Getter
from check_module import Tester
import threading


TESTER_CYCLE = 4  # 设置每一个TESTER线程运行后休眠时间
GETTER_CYCLE = 60  # 设置每一个TESTER线程运行后休眠时间
TESTER_ENABLED = True  # 是否调度TESTER
GETTER_ENABLED = True  # 是否调度GETTER
API_ENABLED = True  # 是否调度API
threading_count = 8  #对TESTER设置线程数
API_HOST = '127.0.0.2'  # web接口地址，端口
API_PORT = 5000


class Scheduler():

    def threading_tester(self):

        tester = Tester()

        while True:

            tester.run()

            time.sleep(TESTER_CYCLE)

    def threading_getter(self):

        getter = Getter()

        while True:

            getter.run()
            time.sleep(GETTER_CYCLE)

    def threading_api(self):

        app.run(API_HOST, API_PORT)

    def run(self):
        print('代理池开始运行')

        if TESTER_ENABLED:

            for i in range(threading_count):

                tester_thread = threading.Thread(target=self.threading_tester)

                tester_thread.start()
        #对GETTER只设置了一个线程，因为获取小规模数量代理速度很快
        if GETTER_ENABLED:

            getter_thread = threading.Thread(target=self.threading_getter)

            getter_thread.start()

        if API_ENABLED:

            self.threading_api()
