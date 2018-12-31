# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid10010056.html']

    def parse(self, response):
        item = AutopjtItem()
        #通过各XPath表达式分别提取商品的名称，价格，链接，评论数等信息
        item["name"] = response.xpath("//a[@class='pic']/@title").extract()
        item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"] = response.xpath("//a[@dd_name='单品评论']/text()").extract()
        #提取后返回item
        yield item
        #接下来通过循环自动爬取31页的数据
        for i in range(1,31):
            url = "http://category.dangdang.com/pg"+str(i)+"-cid10010056.html"
            #通过yield返回Request，并指定要爬取的网址和回调函数
            #实现自动爬取
            yield Request(url,callback=self.parse)