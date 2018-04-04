# -*- coding: utf-8 -*-
import scrapy
import shiyanlougithub.items import ShiyanlougithubItem

class ShiyanlouGithubSpider(scrapy.Spider):
    name = 'shiyanlou_github'
    allowed_domains = ['github.com']

    @property
    def start_urls(self):
        url_tmpl=='https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self, response):
        for repository in response.css('li.public')
            item=ShiyanlougithubItem({
                'name':repository.xpath('.//a[@itemprop="name codeRrpository"]/text()').re_first("\n\s(.*)"),
                'update_time':repository.xpath('.//relative_time/@datetime').extract_first()
                })
                yield item
