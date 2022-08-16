# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import os

from itemadapter import ItemAdapter


# class CsvPipeline(object):
#     # CSV数据，保存
#     def __init__(self):
#         self.file = open('tongren.csv', mode='a', encoding='utf-8', newline='')
#         self.csv_write = csv.DictWriter(self.file, fieldnames=['href','title', 'name','date','text'])
#         self.csv_write.writeheader()
#
#     def process_item(self, item, spider):
#         d = dict(item)
#         self.csv_write.writerow(d)
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()
class TextPipeline(object):
    def __init__(self):
        if not os.path.exists('小说'):
            os.mkdir('小说')

    def process_item(self, item, spider):
        title = item['title']
        text = item['text']
        self.file = open('小说\\' + title+'.txt', mode='w', encoding='utf-8')
        info=title+'\n'+'  '+text
        self.file.write(info)
        return item


    def close_spider(self, spider):
        self.file.close()
