# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobboleArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serial_number = scrapy.Field() # 序号
    title = scrapy.Field() # 文章标题
    create_date = scrapy.Field() # 文章创建日期
    type = scrapy.Field() # 文章类型
    praise_number = scrapy.Field() # 点赞数
    collection_number = scrapy.Field() # 收藏数
    comment_number = scrapy.Field() # 评论数
