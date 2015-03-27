from scrapy.spider import Spider
from scrapy.selector import Selector
from RedditScraper.items import RedditPost

class RedditTechSpider(Spider):
	name = "redTech"
	allowed_domains = ["http://www.reddit.com/r/technology/"]
	start_urls = [
		"http://www.reddit.com/r/technology/"
	]
	
	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)
		
		#Create posts array, a list of RedditPosts
		#Create sel selector for Technology subreddit response
		posts = []
		sel = Selector(response)
		postPage = sel.xpath('//*[@id="siteTable"]').extract()
		
		print postPage