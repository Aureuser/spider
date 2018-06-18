#! /usr/bin/env python
#coding:utf-8
import urllib.request
 
url = 'http://www.kkkkk41.com-www.hhhh64.com/'
# url = 'http://fanyi.youdao.com/'
 
req = urllib.request.Request(url)
req.add_header('User-Agent',' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
