# -*- coding: utf-8 -*-
import scrapy
from ITcase.items import ItcaseItem

class ItcaseSpider(scrapy.Spider):
	name = 'itcase'
	#爬虫域，允许爬虫爬取网站的范围
	allowed_domains = ['itcast.cn']
	# 爬虫在第一次启动时从该网站开始
	start_urls = ['http://www.itcast.cn/channel/teacher.shtml#apython']

	def parse(self, response):
		node_list = response.xpath("//div[@class='li_txt']")
		# 用来存储所有的item字段
		items = []
		for node in node_list:
			item = ItcaseItem()
			item['name'] = node.xpath('./h3/text()').extract()[0]
			item['title'] = node.xpath('./h4/text()').extract()[0]
			item['info'] = node.xpath('./p/text()').extract()[0]
			# print(item)
			items.append(item)
			yield item

		# yield items

