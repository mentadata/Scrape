# -*- coding: utf-8 -*-
import scrapy
import logging


class ZillowSpider(scrapy.Spider):
    name = 'zillow'
    
    start_urls = ['https://www.zillow.com/schaumburg-il-60193/']

    def parse(self, response):
        
        all_urls = []

        for results in response.xpath("//div[@id='search-results']//article"):

            url= results.xpath(".//a[starts-with(@href,'/homedetails')]/@href").extract_first()
            all_urls.append(response.urljoin(url))

        next_page = response.xpath("//li[@class='zsg-pagination-next']/a/@href").extract_first()

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)


        for property_url in all_urls:

            yield scrapy.Request(url=property_url,callback=self.parse_property)

    def parse_property(self,response):

        yield {

            'st_address':response.xpath(".//div[@class='home-details-summary-and-price']//div[contains(@class,'hdp-home-header-st-addr')]/text()").extract_first(),
            'city':response.xpath(".//div[@class='home-details-summary-and-price']//div[contains(@class,'zsg-h2')]/text()").extract_first(),
            'price':response.xpath(".//div[starts-with(@class,'home-details-pricing-floater')]//span[@class='value']/text()").extract_first(),
            'housesize':response.xpath(".//div[@class='home-details-summary-and-price']//h3//span[6]/text()").extract_first(), 
            'zestimate':response.xpath(".//div[@class='zestimate']/div/text()[1]").extract_first(),
            'description':response.xpath(".//div[contains(@class,'home-description')]/div/div/text()").extract_first(),
            'housetype':response.xpath(".//div[starts-with(@class,'home-facts-at')]/div[1]//div[@class='fact-value']/text()").extract_first(),
            'yearbuilt':response.xpath(".//div[starts-with(@class,'home-facts-at')]/div[2]//div[@class='fact-value']/text()").extract_first(),
            'heating':response.xpath(".//div[starts-with(@class,'home-facts-at')]/div[3]//div[@class='fact-value']/text()").extract_first(),
            'cooling':response.xpath(".//div[starts-with(@class,'home-facts-at')]/div[4]//div[@class='fact-value']/text()").extract_first(),
            'parking':response.xpath(".//div[starts-with(@class,'home-facts-at')]/div[5]//div[@class='fact-value']/text()").extract_first(),
            'hoa':response.xpath(".//div[starts-with(@class,'home-facts-at')]/div[6]//div[@class='fact-value']/text()").extract_first(),
            'daysonzillow':response.xpath(".//div[starts-with(@class,'home-facts-at')]/div[7]//div[@class='fact-value']/text()").extract_first(),
            'pricepersqft':response.xpath(".//div[starts-with(@class,'home-facts-at')]/div[8]//div[@class='fact-value']/text()").extract_first(),
            'numberofsaves':response.xpath(".//div[starts-with(@class,'home-facts-at')]/div[9]//div[@class='fact-value']/text()").extract_first(),
            'is_forsale':response.xpath(".//div[starts-with(@class,'home-details-pricing-floater')]//div[@class='status']/text()[2]").extract_first(),
            'masterbedlevel':response.xpath(".//div[contains(@class,'category-group')]//div[1]/div[2]/div[5]//div[@class='fact-value']/text()").extract_first(),
            'thirdbedlevel':response.xpath(".//div[contains(@class,'category-group')]//div[1]/div[2]/div[2]//div[@class='fact-value']/text()").extract_first(),
            'fourthbedlevel':response.xpath(".//div[contains(@class,'category-group')]//div[1]/div[2]/div[3]//div[@class='fact-value']/text()").extract_first(),
            'buildingexterior':response.xpath(".//div[contains(@class,'category-group')][3]/div[2]/div[2]//div[@class='fact-value']/text()").extract_first()


        }

        # st_address = response.xpath(".//div[@class='home-details-summary-and-price']//div[contains(@class,'hdp-home-header-st-addr')]/text()").extract_first()
        # st_address = response.xpath(".//div[@class='home-details-summary-and-price']//div[contains(@class,'hdp-home-header-st-addr')]/text()").extract_first()



