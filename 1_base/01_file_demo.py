# 功能描述  文件功能
# by Shawn
# 开发时间: 2021/7/22 15:28

# a+  a如果文件不存在则创建  + 内容追加
fp =open('D:/text.txt','a+')
# 内容要file指定
print('helloword',file=fp)
fp.close()