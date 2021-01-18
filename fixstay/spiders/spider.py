import scrapy

from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from fixstay.items import FixstayItem


class NikkeiSpider(scrapy.Spider):
	name = 'fixstay'
	allowed_domains = ['www.fixstay.com']
	start_urls = ['https://www.fixstay.com/bg/blog.html']

	def parse(self, response):
		post_links = response.xpath('//div[contains(@class, "article_container")]/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

		pagination_links = response.xpath('//div[@class="pagination"]/a[@rel="next"]/@href')
		yield from response.follow_all(pagination_links, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="art_container"]').getall()
		if description:
			description = remove_tags(str(description[0])).strip()

		item = ItemLoader(item=FixstayItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
