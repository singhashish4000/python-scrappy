import scrapy
import csv


class FetchDoctorDetailsSpider(scrapy.Spider):
    name = "fetch_doctor_details"


    def start_requests(self):
        names_urls=[]
        with open('navi-mumbai_doc.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    url = row[0]
                    names_urls.append(url)
               
                    line_count += 1

        # urls = [
        #     'https://www.credihealth.com/doctors/thane'
        # ]

        for url in names_urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        # data=response.css("div.border-hover a::attr(href)").extract()
        name =  response.css("div.col-sm-8 h1.doctor_name::text".strip()).extract()
        qualification =  response.css("div.col-sm-8 p::text".strip()).extract()

        
    

        yield {
            'Name': response.css("div.col-sm-8 h1.doctor_name::text".strip()).extract(),
            'Qualification': response.css("div.col-sm-8 p::text".strip()).extract(),
            'Fee' :  response.css("div.col-sm-4.margin-t10 div.margin-t10 p.fee::text".strip()).extract(),
            'Rating' : response.css("div.bg-white.padding-20.box-shadow div.col-sm-8 div.col-sm-3.text-center button.btn-like.btn-credi.border-radius-curved::text".strip()).extract(),
            'Place'  : response.css("div.bg-white.padding-20.box-shadow h3.doctor_heading a::text".split(",")[0]).extract(),
            'Image' : response.css("div.col-sm-8 div.col-sm-3.text-center div.rounded-avatar  img::attr(data-original)").extract()
        }