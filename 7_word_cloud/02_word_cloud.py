# 功能描述
# by Shawn
# 开发时间: 2021/8/10 10:43
import jieba
import wordcloud

txt ='Python是一种代表简单主义思想的语言。阅读一个良好的Python程序就感觉像是在读英语一样。它使你能够专注于解决问题而不是去搞明白语言本身。'
words = jieba.lcut(txt)

newword =" ".join(words)
print(newword)
wd = wordcloud.WordCloud(font_path='msyh.ttc',width=500,height=300).generate(newword)
wd.to_file("text.png")