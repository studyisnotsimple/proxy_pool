# proxy_pool
构建的一个轻量级代理池
## 项目描述
    这个项目主要是平时爬虫经常会被网站封IP，所以决定搭个轻型代理池，学习用应该是够了。
## 项目功能描述
    该项目参考了崔庆才 编著的《python3 网络爬虫开发实战》中 <代理池维护> 章节,对其实现做了适合我自己的修改，
    将书中多进程模式改为多线程模式，减小电脑系统负担。对一些功能做了适合自己的精简，但是大佬的功能是很完善的，
    要多多学习。因此，该项目主要利用多线程实现了从代理网站爬取代理IP，然后存储到Redis,接着从Redis里随机抽一
    个ip，对代理ip进行目标网站的可用性验证，然后在Redis中对IP进行加减分数，删除不合格IP等操作。。循环往复达
    到保存一批优质代理IP目的。
## 项目使用指南
    程序从run_start.py文件执行，必须修改的是check_module.py文件下TEST_URL为你想爬取的网站，具体其他修改参
    数，程序里备注都有指明。对于代理IP调用，在浏览器输入：127.0.0.2：5000/random 可以查看，requests这个地
    址即可完成调取。

## 效果展示
pycharm控制台输出
<br>
![1](https://github.com/studyisnotsimple/proxy_pool/blob/master/image/1.png)
<br>
<br>
Redis输出
<br>
![2](https://github.com/studyisnotsimple/proxy_pool/blob/master/image/2.png)
<br>
<br>
web api接口输出
<br>
![3](https://github.com/studyisnotsimple/proxy_pool/blob/master/image/3.png)
<br>
![4](https://github.com/studyisnotsimple/proxy_pool/blob/master/image/4.png)
<br>
![5](https://github.com/studyisnotsimple/proxy_pool/blob/master/image/5.png)
<br>
## 版本
    python3
    win10
## 鸣谢
    在此，感谢，崔庆才 所著《python3 网络爬虫开发实战》，从中受益良多。感谢，58同城作为爬取网站示例所做的牺牲。
    感谢，西拉代理提供的免费代理ip。感谢所有传授给我知识的人。
## 写在最后
    这个代理池项目还挺实用的，发上来也是为了能好好的保存，见证下自己走过的路。
