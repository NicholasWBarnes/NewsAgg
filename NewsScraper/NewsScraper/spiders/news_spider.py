import scrapy

from NewsScraper.items import NewsScraperItem

class NewsSpider(scrapy.Spider):
	name = "lrp"
	allowed_domains = ["littleredpenpublishing.com"]
	start_urls = [
		"http://littleredpenpublishing.com/?page_id=38"
	]
	
	def parse(self, response):

		item = NewsScraperItem()
		item['title'] = response.xpath('/html/head/title/text()').extract()
		item['content'] = response.xpath('//div[@class="entry-content"]/p/text()').extract()
		
		
		print'\n'
		print'\n'
		print item['title']
		print'\n'
		print item['content']
		print'\n'
		print'\n'


		
		
		