#_*_coding:utf-8_*_

import scrapy
import re
from bs4 import BeautifulSoup as bs
from zhilian.items import ZhilianItem

class mapSpider(scrapy.Spider):
	name = "zhilian_map"
	start_urls = ['http://www.zhaopin.com/citymap.html',]
	kw = 'ios'
	def parse(self, response):
		cc = ''
		citys = ['北京','天津','上海','重庆','河北','山西','辽宁','吉林','黑龙江','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','海南','四川','贵州','云南','陕西','甘肃','青海','台湾','内蒙古','广西','西藏','宁夏','新疆','香港','澳门']
		for ct in citys:
		#for citys in response.xpath('//div[@id="letter_choose"]/dl/dd'):
			#for city in citys.xpath('.//a'):
				#if city.xpath('.//strong').extract_first() is not None:
					#city = city.xpath('.//strong')
				#ct = city.xpath('.//text()').extract_first()
			url_city = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=ios&sm=0&p=1' % ct
			yield scrapy.Request(url=url_city, callback=self.parse_jobs)

	def parse_jobs(self,response):
		job_position = response.xpath('//*[@id="JobLocation"]/@value').extract_first()
		for job in response.xpath('//table[@class="newlist"]/tr'):
			kword = job.xpath('.//td[@class="zwmc"]/div/a/b/text()').extract_first()	
			if kword is not None:
				item = ZhilianItem()
				item["job_company"] = job.xpath('.//td[@class="gsmc"]/a/text()').extract_first()
				item["job_price"] = job.xpath('.//td[@class="zwyx"]/text()').extract_first()
				item["job_date"] = job.xpath('.//td[@class="gxsj"]/span/text()').extract_first()
				item["job_name"] = job.xpath('.//td[@class="zwmc"]/div/a/text()').extract_first()
				item["job_position"] = job_position
				item["job_is"] = 1
				yield item
		job_next = response.xpath('//a[@class="next-page"]/@href').extract_first()
		print ("********",job_next)
		if job_next is not None:
			yield scrapy.Request(url=job_next, callback=self.parse_jobs)

