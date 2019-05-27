# -*- coding: utf-8 -*-
from scheduler_module import Scheduler

def main():
    try:
        start = Scheduler()
        start.run()  # 运行调度函数
    except:
        main()

if __name__ == '__main__':
    main()
