# -*- coding: utf-8 -*-
import scrapy


class BioonSpider(scrapy.Spider):
    name = 'bioon'
    # allowed_domains = ['http://login.bioon.com']
    start_urls = ['http://login.bioon.com/login/do_login']
    formdata = {
    'account':'1355087842@qq.com',
    'username':'1355087842@qq.com',
    'password':'15776488761li',
    'checkCode':'',
    'remember':'0',
    'csrf_token':'e8d54bb609213a6b426a9ca651d59061',
    'grant_type':'password',
    'client_id':'usercenter',
    'redirect_uri':'http://login.bioon.com/userinfo',
    'state':'',
    'referer':''
    }

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,formdata = self.formdata, callback = self.after_login)

    def after_login(self,response):
        print('#'*50)
        print(response.url)
