# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ZhilianItem(Item):
	job_name = Field()
	job_company = Field()
	job_price = Field()
	job_position = Field()
	job_date = Field()
	job_is = Field()
