# -*- coding: utf-8 -*-
import scrapy


class LoginSpiderSpider(scrapy.Spider):
    name = 'login_spider'
    #allowed_domains = ['shiyanlou.com/login']
    start_urls = ['https://shiyanlou.com/login']

    def parse(self, response):
        csrf_token=response.xpath('//div[@class="login-body"]//input[@id="csrf_token"]/@value').extract_first()
        self.logger.info(csrf_token)
        return scrapy.FormRequest.from_response(
                response,
                formdata={
                    'csrf_token':csrf_token,
                    'login':'511590474@qq.com',
                    'password':'101402108mynba'
                    },
                callback=self.after_login
                )
    def after_login(self,response):
        return [scrapy.Request(
            url='https://www.shiyanlou.com/user/539049/',
            callback=self.parse_after_login
            )]

    def parse_after_login(self,response):
        return {
            'lab_count':response.xpath('(//span[@class="info-text"])[2]/text()').re_first('[^\d]*(\d*)[^\d*]'),
            'lab_munutes':response.xpath('(//span[@class="info-text"])[3]/text()').re_first('[^\d]*(\d*)[^\d*]')
                }




