# -*- coding: utf-8 -*-
# 项目的管道文件
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ItcasePipeline(object):
    def __init__(self):
    	self.f = open("itcast_pipeline.json","w")

    def process_item(self, item, spider):
    	content = json.dumps(dict(item),ensure_ascii = False) + ', \n'
    	# print(content)
    	self.f.write(content)
    	# print(type(content)) 结果是str
    	return item

	def open_spider(self,spider):
		pass
		# 可选实现，当spider被开启时，这个方法被调用

    def close_spider(self,spider):
    	self.f.close()