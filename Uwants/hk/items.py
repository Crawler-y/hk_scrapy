# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HkItem(scrapy.Item):
    publish_time=scrapy.Field()
    user=scrapy.Field()
    title=scrapy.Field()
    content=scrapy.Field()
    content_url=scrapy.Field()