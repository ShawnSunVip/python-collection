# 功能描述
# by Shawn
# 开发时间: 2021/7/27 14:28

# r 读  w 写 a 追加 b 二进制
print("==============读===================")
file=open('demo.txt','r',1,'utf-8')
print(file.readlines())
print(file.readline())
print(file.read())
print(file.read(2))
print("文件当前指针",file.tell())
file.close()

#用完会自动关闭
with open('demo.txt','r',1,'utf-8') as filewith:
    print(filewith.read())

print("===============写==================")
file2=open('demo02.txt','w',1,'utf-8')
file2.write('你好，python')
file2.close()

print("================文件=================")
file3 =open('dapao.jpg','rb')
file4 =open('copy_dapao.jpg','wb')
file4.write(file3.read())
file3.close()
file4.close()