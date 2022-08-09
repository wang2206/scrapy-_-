# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter

from .items import Qd04GuokeItem


class CsvPipeline(object):
    # CSV数据，保存
    def __init__(self):
        self.file = open('cas.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.file, fieldnames=['title', 'span', 'data'])
        self.csv_write.writeheader()

    def process_item(self, item, spider):
        d = dict(item)
        self.csv_write.writerow(d)
        return item

    def close_spider(self, spider):
        self.file.close()