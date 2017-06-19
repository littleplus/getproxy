# getproxy

English:

This project with the purpose of getting the regular proxy server list.


It will be formatted as belowing:

127.0.0.1 8080  Localhost

split items with "\t" and split each server with "\n"

You can use Python command "split" to get them easily.

Dependence:

Python 2.6~3.6.1
requests
bs4

You can run

pip install requests
pip install bs4

to install the dependence



中文:

一个简单的获取有规则的代理IP列表的脚本，格式如下：

127.0.0.1 8080  Localhost

使用"\t"分隔每个元素，使用"\n"换行，使用Python的split可以很方便的获取每个元素

环境依赖：

目前在Python2.6~3.6.1都能正常运行，需要先安装requests和bs4

可以通过以下命令安装：

pip install requests
pip install bs4

