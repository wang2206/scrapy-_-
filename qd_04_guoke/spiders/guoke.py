import time

import scrapy

from ..items import Qd04GuokeItem


class GuokeSpider(scrapy.Spider):
    name = 'guoke'
    allowed_domains = ['guokr.com']
    start_urls = ['https://www.guokr.com/mine/bkfczo']

    def parse(self, response):
        spans = response.css('.styled__ArticleWrap-hzwv3e-0.duYTFf.panel-article')
        for div in spans:
            time.sleep(2)
            title = div.css('.layout__Skeleton-zgzfsa-3.styled__InfoTitileWrap-hzwv3e-3.jjIdbw::text').get()
            span = div.css('.cVBiFR>span::text').get()
            data = div.css('.nickname::text').get()
            ite = Qd04GuokeItem(title=title, span=span, data=data)
            yield ite
