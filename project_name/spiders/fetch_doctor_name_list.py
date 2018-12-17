import scrapy
import csv


class FetchDoctorNamesSpider(scrapy.Spider):
    name = "fetch_doctor_names_list"


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
        name = response.css("div.center-section div.doc-list.border-hover span.no-decoration::text").extract()
       
        i=0;
        for value in name:
            name[i]=name[i]
            i=i+1

        for url in name:
            yield {
                'Name': url
            }   