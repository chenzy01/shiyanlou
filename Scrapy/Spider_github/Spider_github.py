# -*- coding: utf-8 -*-
import scrapy

class GithubSpider(scrapy.Spider):
    #命名爬虫的名字
    name='shiyanlou-github'
   # '''
   # def start_requests(self):
   #     url_tmpl='https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
       #提取22个网页的网址形成一个元组
   #     urls=(url_tmpl.format(i) for i in range(1,23))
   #     for url in urls:
            #url指明要爬取的网页，self.parse提取数据
   #         yield scrapy.Request(url=url,callback=self.parse)
   # '''
    @property
    def start_urls(self):
        url_tmpl='https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        for repository in response.css('li.public'):
            yield{
                    'name':repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
                    'update_time':repository.xpath('.//relative-time/@datetime').extract_first()
            }

