# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
from hk.items import HkItem

class HkSpider(scrapy.Spider):
    name = 'HK'
    allowed_domains = ['uwants.com','yahoo.com','hkgolden.com']
    def start_requests(self):
        #需要搜索的关键词
        keyword='Uwants'#
        #################
        base_url='https://hk.forum.search.yahoo.com/search?p={}&fr=uwants&flt=sort:time'
        yield Request(url=base_url.format(keyword))
    def parse(self, response):
        base_url='http://www.uwants.com/viewthread.php?tid={}&extra=&page={}'
        rsps=response.xpath('//div[@id="web"]/ol[2]/li/div/div/div[1]/h3/a/@href')
        content_page=1
        for i in rsps:
            content_url=i.extract()
            re_user=re.findall('%3d(\S*)%26|%3d(\S*)/',content_url)
            for i in re_user:
                dat=''.join(i)
                try:
                    user_id=dat.split('/')
                    if len(user_id[0]) >=6:
                        yield Request(url=base_url.format(user_id[0],str(content_page)),callback=self.parse_content)
                        # content_page+=1
                except:
                    yield Request(url=base_url.format(dat,str(content_page)),callback=self.parse_content)
                    # content_page += 1
        # 翻页连接
        page=re.findall(r'&b=(\d+)',response.url)
        try:
            tmp=response.xpath('//a[contains(text(),"下一頁")]/@href').extract()[0]
            next_page=re.findall(r'&b=(\d+)',tmp)
            if page != next_page:
                yield Request(url=tmp)
        except:
            print('已是全部数据了')
    ###########################################################################
    def parse_content(self,response):
        item = HkItem()
        base_nodes=response.xpath('//div[contains(@class,"mainbox viewthread")]')
        title=base_nodes.xpath('.//span[contains(@class,"headactions")]/following-sibling::h1[1]/text()').extract()[0]
        for node in base_nodes:
            user=node.xpath('.//cite/div/following-sibling::a[1]/text()').extract_first()
            tmp=''.join(node.xpath('.//td[@class="postcontent"]/div/text()').extract()).replace('\xa0','').replace('\t','').replace('\n','')
            template = re.compile(r'發表於\s+(.*?\s+.*?\s+.*?)\s+')
            publish_time= template.findall(tmp)[0]
            content=''.join(node.xpath('./table//tr[1]/td[2]/div[3]//div[contains(@id,"postmessage_")]/span//text()|./table//tr[1]/td[2]/div[3]//div[contains(@id,"postmessage_")]/span//img/@src').extract()).replace('\n','').replace('\t','')
            item['user']=user
            item['publish_time']=publish_time
            item['title']=title
            item["content"]=content
            item['content_url']=response.url
            yield item

