# -*- coding: utf-8 -*-
import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['theater.mtime.com']
    start_urls = ['http://theater.mtime.com/China_Yunnan_Province_Yuxi/']

    def parse(self, response):
        pass
