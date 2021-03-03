#男生必学的第一步
#爬图片

import re
import os
import urllib
import urllib.request

def get_url(url):
    page =urllib.request.urlopen(url)
    html =page.read()
    return html.decode("utf-8")

def get_img(html):
    reg = r'https://[^\s]*?\.jpg'
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

htmls =get_url("http://www.netbian.com")
print(get_img(htmls))
