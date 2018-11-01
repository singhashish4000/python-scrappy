import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.credihealth.com/doctors'
        ]
        location_urls=[]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        # data=response.css("div.border-hover a::attr(href)").extract()
        location =  response.css('a.city_link').xpath('@href').extract()
        i=0;
        for value in location:
            print(location[i])
            location[i]='https://www.credihealth.com'+location[i]
            i=i+1
            # data[key]='https://www.credihealth.com/'.item


        print(location)

        for url in location:
            yield {
                'location': url
            }

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'location-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)
        # filename = 'URL-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(data)
        # self.log('Saved file %s' % filename)