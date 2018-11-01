# -*- coding: utf-8 -*-
import scrapy
#from scrapy.selector import Selector


class CredihealthSpider(scrapy.Spider):
    name = 'credihealth'
    allowed_domains = ['www.credihealth.com']
    start_urls = ['https://www.credihealth.com/doctors/mumbai']
    doctors_urls=[]
    #for href in sel.css("div.recipe-description a::attr(href)").extract():
    #print href
    def parse(self, response):
        #sel = Selector(response)
        #print(response)
        data=response.css("div.border-hover").extract()
        for div in data:
            yield {'url':div.css("a::attr(href)")}
          #  print(href)

          
    pass
