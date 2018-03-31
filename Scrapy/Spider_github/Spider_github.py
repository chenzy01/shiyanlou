# -*- coding: utf-8 -*-
import scrapy

class GithubSpider(scrapy.Spider):
    #�������������
    name='shiyanlou-github'
   # '''
   # def start_requests(self):
   #     url_tmpl='https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
       #��ȡ22����ҳ����ַ�γ�һ��Ԫ��
   #     urls=(url_tmpl.format(i) for i in range(1,23))
   #     for url in urls:
            #urlָ��Ҫ��ȡ����ҳ��self.parse��ȡ����
   #         yield scrapy.Request(url=url,callback=self.parse)
   # '''
    @property
    def start_urls(self):
        url_tmpl='https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.formit(i) for i in range(1,5))

    def parse(self,response):
        for repository in response.css('li.public'):
            yield{
                    'name':repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
                    'update_time':repository.xpath('.//relative-time/@datetime').extract_first()
            }

