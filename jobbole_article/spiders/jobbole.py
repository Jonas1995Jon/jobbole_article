# -*- coding: utf-8 -*-
import re
from urllib.parse import urljoin

import scrapy
from jobbole_article.items import JobboleArticleItem

class JobboleSpider(scrapy.Spider):
    def __init__(self):
        self.num = 0
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        url_list = response.css("div#archive > div.post > div.post-thumb > a::attr(href)").extract()
        for url in url_list:
            yield scrapy.Request(url, callback=self.parse_detail)

        next_url = response.css("div#archive > div.navigation.margin-20 > a.next.page-numbers::attr(href)").extract()[0]
        if next_url:
            yield scrapy.Request(urljoin('blog.jobbole.com', next_url), callback=self.parse)

    def parse_detail(self, response):
        self.num = self.num + 1
        acticleItem = JobboleArticleItem()
        acticleItem['serial_number'] = self.num
        acticleItem['title'] = response.css("div.entry-header > h1::text").extract_first()
        create_date = response.css("div.entry-meta > p::text").extract_first()
        acticleItem['create_date'] = create_date.strip().replace('·', '').strip()
        types = response.css("div.entry-meta > p > a::text").extract()
        type = '·'.join(types)
        acticleItem['type'] = type
        praise_number = response.css("div.post-adds span.vote-post-up h10::text").extract_first()
        if praise_number and praise_number.isdigit():
            acticleItem['praise_number'] = praise_number
        else:
            acticleItem['praise_number'] = 0
        collection_number = response.css("div.post-adds span.bookmark-btn::text").extract_first().strip()
        reg = '.*(\d+).*'
        collection_number_reg = re.match(reg, collection_number)
        if collection_number_reg:
            acticleItem['collection_number'] = int(collection_number_reg.group(1))
        else:
            acticleItem['collection_number'] = 0
        comment_number = response.css("div.post-adds > a span.hide-on-480::text").extract_first().strip()
        comment_number_reg = re.match(reg, comment_number)
        if comment_number_reg:
            acticleItem['comment_number'] = int(comment_number_reg.group(1))
        else:
            acticleItem['comment_number'] = 0
        yield acticleItem