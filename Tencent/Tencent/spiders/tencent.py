# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    bestURL = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [bestURL + str(offset)]

    def parse(self, response):
        print("#"*80)
        node_list = response.xpath("//tr[@class='even'] | //tr[@class = 'odd']")
        for node in node_list:
            item = TencentItem()
            item["positionName"] = node.xpath("./td[1]/a/text()").extract()[0].encode("utf-8")
            item["positionLink"] = node.xpath("./td[1]/a/@href").extract()[0].encode("utf-8")
            if node.xpath("./td[2]/text()"):
                item["positionType"] = node.xpath("./td[2]/text()").extract()[0].encode("utf-8")
            else:
                item["positionType"] = ''
            item["peopleNumber"] = node.xpath("./td[3]/text()").extract()[0].encode("utf-8")
            item["workLocation"] = node.xpath("./td[4]/text()").extract()[0].encode("utf-8")
            item["publishTime"] = node.xpath("./td[5]/text()").extract()[0].encode("utf-8")
            yield item
        # print(response.xpath("//a[@class = 'noactive'and @id = 'next']"))
        if not response.xpath("//a[@class = 'noactive'and @id = 'next']"):
            url = "https://hr.tencent.com/" + response.xpath("//a[@id = 'next']/@href").extract()[0]
            print(url)
            yield scrapy.Request(url = url,callback = self.parse,dont_filter=True)