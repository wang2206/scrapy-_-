import re

import scrapy

from ..items import Qd09TongrenItem_02


class TongrenSpider(scrapy.Spider):
    name = 'tongren_02'
    allowed_domains = []
    # start_urls = [f'https://www.tongrenquan.org/tags-150-{page}.html' for page in range(0,52)]
    start_urls = [f'https://www.tongrenquan.org/tongren/6715/{page}.html' for page in range(1,432)]

    def parse(self, response):
        title = response.xpath('//div[@class="read_chapterName tc"]/h1/text()').extract_first()
        text=response.xpath('//div[@class="read_chapterDetail"]/p/text()').extract()
        text='\n'.join(text)
        yield Qd09TongrenItem_02(title=title,text=text)

