# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import zaobaoItem

class ZaobaoSpider(scrapy.Spider):
    name = 'zaobao2'
    allowed_domains = ['http://www.zaobao.com']
    start_urls = ['http://www.zaobao.com/special/report/politic/fincrisis']
    title_xpath = "//span[@class='post-title']/text()"
    time_xpath = "//span[@class='datestamp']/text()"
    body_xpath = "//div[@id = 'FineDining']/p/strong/text() | //div[@id = 'FineDining']/p/text()"
    link_xpath = '//a[@data-path="special/report/politic/fincrisis"]/@href'
    def get_body(self,url):# abc
        body = scrapy.Request(url)
        body = body.body.xpath("//div[@id = 'FineDining']/p/strong/text() | //div[@id = 'FineDining']/p/text()").extract()
        strs = ''
        for i in body:
            strs += i
        return strs


    def set_body(self,response):
        # print('#'*50)
        item = response.meta['item']
        body = response.xpath("//div[@id = 'FineDining']/p/strong/text() | //div[@id = 'FineDining']/p/text()").extract()
        strs = ''
        for i in body:
            strs += i
        item['body'] = strs
        return item

    def parse_next(self, response):
        item = zaobaoItem()
        item['title'] = response.xpath('//div[@class="body-content"]/h1/text()').extract()[0]
        item['time'] = response.xpath('//div[@class="body-content"]//span[@class="datestamp date-published meta-date-published"]').extract()[0].split('</i>')[1].split('<em>')[0] +  response.xpath('//div[@class="body-content"]//span[@class="datestamp date-published meta-date-published"]').extract()[0].split('</i>')[1].split('<em>')[1].split('</em>')[0]
        body = response.xpath("//div[@id = 'FineDining']/p/strong/text() | //div[@id = 'FineDining']/p/text()").extract()
        strs = ''
        for i in body:
            strs += i
        item['body'] = strs
        item['link'] = response.url
        return item

    def parse(self, response):
        # 得到的类型为list
        titles = response.xpath("//span[@class='post-title']/text()").extract()
        times = response.xpath("//span[@class='datestamp']/text()").extract()
        links = [response.xpath('//a[@data-path="special/report/politic/fincrisis"]/@href').extract()[x*2] for x in range(20)]
        print(len(titles))
        print(len(times))
        print(len(links))
        for x in range(20):
            item = zaobaoItem()
            url = 'http://www.zaobao.com' + links[x]
            body = self.get_body(url)
            item['body'] = body
            item['title'] = titles[x]
            item['time'] = times[x]
            item['link'] = url
            yield item
        # for link in links:
        #     url = 'http://www.zaobao.com' + link
        #     yield scrapy.Request(url=url,callback = self.parse_next,dont_filter=True)