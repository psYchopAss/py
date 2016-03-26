#<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102elmo.html">2013年09月27日</a>
#coding:utf-8
import urllib.request
stro = '<a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102egl0.html">地震思考录</a>'
title = stro.find(r'<a title')
print (title)
href = stro.find(r'href=')
print (href)
html = stro.find(r'html')
print (html)
url = stro[href+6:html+5]
print(url)
content = urllib.request.urlopen(url).read()
print (content)

