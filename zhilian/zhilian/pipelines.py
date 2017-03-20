# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from scrapy.exceptions import DropItem

class ZhilianPipeline(object):
	def process_item(self, item, spider):
		price = item["job_price"]
		ma = re.match(r'\d+-\d+',price)
		if ma is not None:
			prices = price.split('-')
			price = (int(prices[0]) + int(prices[1])) / 2
			item['job_price'] = price
			return item
		else:
			raise DropItem("Missing price in %s" % item) 

