# -*- coding:utf-8 -*-

import scrapy
from shiyanlou.items import CourseItem

class CoursesSpider(scrapy.Spider):
    #命名爬虫的名字
    name='courses'
#    '''
#    def start_requests(self):
#        url_tmpl='https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
       #提取22个网页的网址形成一个元组
#        urls=(url_tmpl.format(i) for i in range(1,23))
#        for url in urls:
            #url指明要爬取的网页，self.parse提取数据
#            yield scrapy.Request(url=url,callback=self.parse)
#    '''
    @property
    def start_urls(self):
        url_tmpl='https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=a    ll&tag=all&page={}'
        return (url_tmpl.format(i) for i in range(1,23))

    def parse(self,response):
        for course in response.css('div.course-body'):
            item=CourseItem({
                    'name':course.css('div.course-name::text').extract_first(),
                    'description':course.css('div.course-desc::text').extract_first(),
                    'type':course.css('div.course-footer span.pull-right::text').extract_first(),
                    'students':course.xpath('.//span[contains(@class,"pull-left")]/text()[2]').re_first('[^\d]*(\d)[^\d]*')
                    })
            yield item

