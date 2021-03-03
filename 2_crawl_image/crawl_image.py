#男生必学的第一步
#爬图片

#注意点
#1.网址的编码规则，根据不同编码做动态修改
#   鼠标右击页面，查看源码 可以知道当前编码
#2.图片匹配规则
#   看清楚需要爬虫的图片的格式是https还是http
#   看清需要爬虫的图片的后缀是jpg还是png

import re
import os
import urllib
import urllib.request

def get_url(url,decode):
    page =urllib.request.urlopen(url)
    html =page.read()
    return html.decode(decode)

def get_img(html):
    reg = r'http://[^\s]*?\.jpg'
    # 转换成一个正则对象
    imgre = re.compile(reg)
    # 表示在整个网页过滤出所有图片的地址，放在imgList中
    imglist = imgre.findall(html)
    # 声明一个变量赋值
    x = 0
    # 设置图片的保存地址
    path = 'E:\Python\images'
    if not os.path.isdir(path):
        # 判断没有此路径则创建
        os.makedirs(path)
    # 保存在mages路径下
    paths = path + '\\'
    for imgurl in imglist:
        # 打开imgList,下载图片到本地
        urllib.request.urlretrieve(imgurl, '{0}{1}.jpg'.format(paths, x))
        print('图片(%s)开始下载，注意查看文件夹' %( str(x)+".jpg"))
        x = x + 1
    return imglist

htmls =get_url("https://tieba.baidu.com/p/7222864124","utf-8")
print(get_img(htmls))
