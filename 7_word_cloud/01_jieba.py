# 功能描述
# by Shawn
# 开发时间: 2021/8/10 10:37
import jieba

str = 'Python是一种代表简单主义思想的语言。阅读一个良好的Python程序就感觉像是在读英语一样。它使你能够专注于解决问题而不是去搞明白语言本身。'
print(jieba.lcut(str))
print(jieba.lcut(str,cut_all=True))