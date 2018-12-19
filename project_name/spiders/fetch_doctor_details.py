import scrapy
import csv


class FetchDoctorDetailsSpider(scrapy.Spider):
    name = "fetch_doctor_details"


    def start_requests(self):
        names_urls=[]
        with open('bangalore_doc.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    url = row[0]
                    names_urls.append(url)
               
                    line_count += 1



        for url in names_urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        # data=response.css("div.border-hover a::attr(href)").extract()
        name =  response.css("div.col-sm-8 h1.doctor_name::text").extract()
        qualification =  response.css("div.col-sm-8 p::text").extract()
        fee = response.css("div.col-sm-4.margin-t10 div.margin-t10 p.fee::text").extract()
        rating = response.css("div.bg-white.padding-20.box-shadow div.col-sm-8 div.col-sm-3.text-center          button.btn-like.btn-credi.border-radius-curved::text").extract()
        place = response.css("div.bg-white.padding-20.box-shadow h3.doctor_heading a::text".split(",")          [0]).extract()
        # image = response.css("div.col-sm-8 div.col-sm-3.text-center div.rounded-avatar  img::attr(data-original)").extract()
        final_fee = ""
        final_rating = ""
        if fee != []:
          final_fee = fee[0].replace("Fees: INR ","")
        else:
          final_fee = '-'

        if rating != "":
            final_rating = rating[1].strip().replace("%","")
        else:
            final_rating = '-'      

          

        yield {
            'Name': name[0].strip(),
            'Qualification': qualification[0].strip(),
            'Fee(INR)' :  final_fee,
            'Rating(%)' : final_rating,
            'Place'  : place[0].strip(),
        }