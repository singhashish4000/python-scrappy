import scrapy
import csv


class FetchDoctorNamesSpider(scrapy.Spider):
    name = "fetch_doctor_names"


    def start_requests(self):
        location_urls=[]
        with open('urls.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    url = row[0]
                    location_urls.append(url)
               
                    line_count += 1
        urls = [
            'https://www.credihealth.com/doctors/agra'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        # data=response.css("div.border-hover a::attr(href)").extract()
        location =  response.css("div.doc-list a::attr(href)").extract()
       
        i=0;
        for value in location:
            print(location[i])
            location[i]='https://www.credihealth.com'+location[i]
            i=i+1
            # data[key]='https://www.credihealth.com/'.item


       

        for url in location:
            yield {
                'Url': url
            }