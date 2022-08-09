import time

import scrapy

from ..items import Qd05KfcItem

'''
关于 post 请求 和 翻页提取数据的命令

FormRequest函数
meta 命令:
   用于两个函数之间传递参数
   一次的，每一次创建request对象都会重新创建
   是一个字典

'''


class KfcSpider(scrapy.Spider):
    name = 'KFC'
    allowed_domains = ['kfc.com.cn']

    # start_urls = ['http://kfc.com.cn/']
    def start_requests(self):
        yield scrapy.FormRequest('http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                                 formdata={
                                     'cname': '',
                                     'pid': '',
                                     'keyword': '北京',
                                     'pageIndex': '1',
                                     'pageSize': '10'
                                 },
                                 callback=self.parse,
                                 # meta 用来翻页
                                 meta={
                                     'page': 2
                                 }
                                 )

    def parse(self, response):
        data_json = response.json()
        data_list = data_json['Table1']
        for data in data_list:
            rownum = data['rownum']
            storeName = data['storeName']
            addressDetail = data['addressDetail']
            pro = data['pro']
            cityName = data['cityName']
            item = Qd05KfcItem(rownum=rownum, storeName=storeName, addressDetail=addressDetail, pro=pro,
                               cityName=cityName)
            yield item
        time.sleep(1)
        print('传下来的 meta:', response.meta.get('page'))
        page = response.meta.get('page')
        if page <= 11:
            yield scrapy.FormRequest('http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                                     formdata={
                                         'cname': '',
                                         'pid': '',
                                         'keyword': '北京',
                                         'pageIndex': str(page),
                                         'pageSize': '10'
                                     },
                                     callback=self.parse,
                                     meta={
                                         'page': page + 1
                                     }
                                     )
