# -*- coding: utf-8 -*-
import scrapy
from scrapy.mail import MailSender

class VwrSpider(scrapy.Spider):
    name = 'vwr'
    allowed_domains = ['qr.vwr.com']
    start_urls = ['https://qr.vwr.com/doc?c=26810.298&b=18D044122']

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
                                                formname="QrCodeCountry",
                                                formdata={"country": "fr_FR,en_FR",
                                                          "catalogNumber": "26810.298",
                                                          "batchNumber": "18D044122",
                                                          "locale": "null"},
                                                callback=self.after_country)

    def after_country(self, response):
        #from scrapy.shell import inspect_response
        #inspect_response(response, self)
        #print(response.xpath('//div[@id="coaCertContainer"]/a/@href').extract())
        coa = response.xpath('//div[@id="coaCertContainer"]/a/@href').extract()
        #mailer = MailSender()
        #mailer.send(to=['romain.bedert@gmail.com'], subject='Essai scrapy', body=coa)
