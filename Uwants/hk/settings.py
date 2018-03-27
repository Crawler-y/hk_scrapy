# -*- coding: utf-8 -*-
BOT_NAME = 'hk'
SPIDER_MODULES = ['hk.spiders']
NEWSPIDER_MODULE = 'hk.spiders'
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
ITEM_PIPELINES = {
   'hk.pipelines.HkPipeline': 300,
}
