# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


from itemadapter import ItemAdapter

# class Qd03EnglishPipeline:
#     def process_item(self, item, spider):
#         return item
#
import csv

from .items import Qd03EnglishItem, Qd03EnglishItem_2


class CsvPipeline(object):
    # CSV数据，保存
    def __init__(self):
        self.file = open('english.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.file, fieldnames=['title', 'text'])
        self.csv_write.writeheader()

        self.file_2 = open('english_2.csv', mode='w', encoding='utf-8', newline='')
        self.csv_write_2 = csv.DictWriter(self.file_2, fieldnames=['title', 'text', 'html_url','img_url'])
        self.csv_write_2.writeheader()

    def process_item(self, item, spider):
        # data = dict(item)
        # self.csv_write.writerow(data)
        # return item
        data = dict(item)
        # 如果得到的 item 对象,是由 Qd03EnglishItem 数据结构对象返回
        if isinstance(item, Qd03EnglishItem):
            self.csv_write.writerow(data)

        # 如果得到的 item 对象,是由 Qd03EnglishItem_2 数据结构对象返回
        elif isinstance(item, Qd03EnglishItem_2):
            self.csv_write_2.writerow(data)
        return item

    def close_spider(self, spider):
        self.file.close()
        self.file_2.close()
