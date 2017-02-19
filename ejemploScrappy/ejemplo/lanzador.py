# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


settings = get_project_settings()
settings.overrides['FEED_FORMAT'] = 'json'
settings.overrides['FEED_URI'] = 'result.json'

process = CrawlerProcess(settings)

# 'followall' is the name of one of the spiders of the project.
process.crawl('spyder', start_urls=['http://quotes.toscrape.com/tag/humor/'])
process.start() # the script will block here until the crawling is finished
