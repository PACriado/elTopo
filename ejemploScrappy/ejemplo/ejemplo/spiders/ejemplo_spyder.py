# -*- coding: utf-8 -*-

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "spyder"

    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]



    def parse(self, response):
        for headElement in response.css('head'):
            yield {
                'title': headElement.css('title').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
