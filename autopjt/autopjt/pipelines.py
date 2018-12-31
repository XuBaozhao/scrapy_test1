# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
#因为要进行JSON文件的处理，所以导入json模块
import json

class AutopjtPipeline(object):
    def __init__(self):
        #以写入的方式创建或打开mydata.json文件
        #self.file = codecs.open("D:/python_new/autopjt/mydata.json","wb",encoding="utf-8")
        self.file = codecs.open("D:/python_new/autopjt/mydata.json2", "wb", encoding="utf-8")
    def process_item(self, item, spider):
        #通过jict(item)将item转化为一个字典
        #然后通过json模块下的dumps()处理字典数据
        #i = json.dumps(dict(item),ensure_ascii=False)
        #每条数据后加上换行，形成要写入的一行数据
        #line = i + '\n'
        #数据写入到mydata.json文件中
        #self.file.write(line)
        #return item
        for j in range(0,len(item["name"])):
            name = item["name"][j]
            price = item["price"][j]
            comnum = item["comnum"][j]
            link = item["link"][j]
            #将当前页下的第j个商品的name、price、comnum、link信息处理一下
            #重新组合称一个字典
            goods = {"name":name,"price":price,"comnum":comnum,"link":link}
            #将当前页下第j各商品的数据写入json文件
            i = json.dumps(dict(goods),ensure_ascii=False)
            line = i+'\n'
            self.file.write(line)
        return item

    def close_spider(self,spider):
        #关闭mydata.json文件
        self.file.close()