import time

import scrapy

from ..items import Qd03EnglishItem, Qd03EnglishItem_2


class EnglishSpider(scrapy.Spider):
    name = 'english'
    allowed_domains = ['chinadaily.com.cn']
    start_urls = [f'http://language.chinadaily.com.cn/thelatest/page_{page}.html' for page in range(1,535)]
    # start_urls = ['http://language.chinadaily.com.cn/thelatest/']

    def parse(self, response):
        time.sleep(2)
        divs=response.css('.gy_box')
        for div in divs:
            title=div.css('.gy_box_txt .gy_box_txt2 a::text').get().strip()
            text=div.css('.gy_box_txt .gy_box_txt3 a::text').get().strip()
            item=Qd03EnglishItem(title=title,text=text)
            yield item
            #保存链接和图片链接地址
            html_url=div.css('.gy_box_img::attr(href)').get().strip()
            html_url='http:'+html_url
            img_url=div.css('.gy_box_img img::attr(src)').get().strip()
            new_img=Qd03EnglishItem_2(title=title,text=text,html_url=html_url,img_url=img_url)
            yield new_img

