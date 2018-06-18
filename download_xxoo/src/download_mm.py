#! /usr/bin/env python
#coding:utf-8

import urllib.request
import os

page_numbers = 0
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
#     print(html)
    img_addr = []
    a = html.find('/htm/2018/3/27/p02/')
    while a != -1:
        b = html.find('" target="',a,a+40)
        if b != -1:
            img_addr.append(html[a:b])
#             print(html[a:b])
        else:
            b = a+9
            
        a = html.find('/htm/2018/3/27/p02/',b)
        
    return img_addr
    
def file_imgs(url):
    html = url_open(url).decode('utf-8')
#     print(html)
    img_addr = []
    a = html.find('<img src="')
    while a != -1:
        b = html.find('" border=',a,a+255)
        if b != -1:
            img_addr.append(html[a+10:b])
#             print(html[a:b])
        else:
            b = a+9
            
        a = html.find('<img src="',b)
        
    return img_addr
    
def save_imgs(flname,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-2]+'.'+each.split('/')[-1]
        with open(filename,'wb') as p:
            p.write(url_open(each))
        global page_numbers
        page_numbers=page_numbers+1
        print(page_numbers)
    
def download_mm(flname='xxoo',pages=10):
    os.mkdir(flname)
    os.chdir(flname)
    
    url_p2 = 'http://www.kkkkk41.com-www.hhhh64.com/p02/index.html'
    url = 'http://www.kkkkk41.com-www.hhhh64.com'
    page_num = get_page(url_p2)
#     print(page_num)
    for i in page_num:
        page_url = url+i
#         print(page_url)
        img_addrs = file_imgs(page_url)
#         print(img_addrs)
        save_imgs(flname,img_addrs)
    
if __name__ == '__main__':
    download_mm()