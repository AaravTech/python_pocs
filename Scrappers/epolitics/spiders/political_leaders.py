# -*- coding: utf-8 -*-
import scrapy
import time
import json

class PoliticalLeadersSpider(scrapy.Spider):
    name = 'political_leaders'
    allowed_domains = ['www.thefamouspeople.com']
    start_urls = ['https://www.thefamouspeople.com/indian-political-leaders.php']

    custom_settings = {
        'FEED_URI' : 'tmp/political_leaders.csv'
    }

    def parse(self, response):
        row = {}
        for data in response.css('.quickfactsdata'):
            key = data.css('span.quickfactstitle::text').get()
            key = key.strip().split(':')[0].lower()
            value = data.css('.quickfactsdata::text').get()
            if isinstance(value, str):
                value = value.strip()

            if key == "siblings":
                value = [v.strip() for v in value.split(",")]
            row[key] = value
        # print(json.dumps(row, indent=4))
        if row:
            yield row

        leaders_links = response.css('.catprofiles a::attr(href)').getall()
        for leader_link in leaders_links:
            if leader_link is not None:
                time.sleep(2)
                leader_link = response.urljoin(leader_link)
                yield scrapy.Request(leader_link, callback=self.parse)
            # break