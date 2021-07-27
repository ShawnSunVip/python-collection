# 功能描述  定时job
# by Shawn
# 开发时间: 2021/7/27 14:18

import schedule

def sayHelloJob():
    print("哈喽！！！")

schedule.every(3).seconds.do(sayHelloJob)

if __name__ == '__main__':
    while True:
        schedule.run_pending()