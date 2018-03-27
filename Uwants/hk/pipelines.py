# -*- coding: utf-8 -*-

import os
import csv

class HkPipeline(object):
    def process_item(self, item, spider):
        # 存放路径
        os.chdir('D:\My Documents\Desktop\hk\hk\spiders')
        with open('Uwants.csv', 'a',newline='')as f:
            writer = csv.writer(f)
            try:
                print('进行utf-8编码处理')
                item['content'].encode('uft-8') and item['user'].encode('utf-8')
                writer.writerow(( item['user'],item['publish_time'],item['title'],item['content']))
            except:
                print('进行gbk编码处理')
                item['content'].encode('gb18030') and item['title'].encode('gb18030')
                writer.writerow(( item['user'],item['publish_time'],item['title'],item['content'],item['content_url']))
            finally:
                return item
