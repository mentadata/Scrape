import scrapy
import json

class Sooper1PostSpider(scrapy.Spider):
    name='sooper1'

    payload = '''

        {"upcs":["0001820025001","0007089701331","0008382010401","0008066095615","0007825000328","0001820053168","0008382012393","0001820025000","0008066095757","0003410057306","0063598554890","0007089718331","0007199030065","0008066095715","0008066095710","0008382012368","0007289000016","0008066095605","0001820005990","0001820096715","0001820006991","0001820000769","0007199009511","0001820000833"],"filterBadProducts":true,"clicklistProductsOnly":false}

    '''

    reqCookie = '''

        JSESSIONID=5ACF60F9E0A98701081EA13697E5EB63; pid=277cbf83-b283-44ec-802d-605f224e8692; origin=lvdc; sid=ffbb1e77-e04f-7c2c-71c8-9685bf5b1d1a; akaalb_KT_Digital_BannerSites=~op=KT_Digital_BannerSites_Legacy:kcvg|~rv=21~m=kcvg:0|~os=49d9e32c4b6129ccff2e66f9d0390271~id=2b2e1d8ff9ab47192b458a443ab25a1f; bm_sz=110F1F65166D1073779D7BBE29787236~YAAQPrYtFy9ITbBpAQAAIOz/sAPBpWnmJUwd3z6Tx4rGIHSgJDmPvqyixA3VVgHWnp2+Qp9B235C5I8NOrSvwnG8n+vqX1Ah1f8AsvZCHSKht5uEniNXvgzD3WpRBHkeaZO7ZNoubSLZq3tiqlhR5cerEy9tDWqCb8FSTexVt17D6YHgc7eLd+O3Dk4SVzU3/zB0bzM=; ak_bmsc=0D42D3455D8A90B13F383CBD367092CA172DB63E1B440000D3CE975C7ECD9348~pl9q8Q8bSp0YFjZulnoYkjfwKMvqVYBTYCtMqvPiBnDXBprevcBbTYfD+QkdVIufJCJTFuD+L8yI0HEhnNmAmfwN/WjG3zrQbrEvWsqQuSYr9kd4opJyK1QNtj8Gay9vcTueEreB8YmjwK1DnTQdy2N2KfFLNk1NR3J8B3LeKcL8yKg8tdun86Ip9v3drJe1w2p2XlJlEjXylPTNGxW8Lej14pButQqJoUDvX11/3RzY7EqOJkn7Hj+pJzVGAc41RV9+f/McoOxS2JHVdT/hU4nUFlUkJod8S1Ro5SZXhlb4JvQyMLK8qxE5mP8X/nwDtXwj9TRQnNJMpqLZUUk5u9Ew==; rxVisitor=1553452760663JHARLV4JVH82DCR1IFPBEKG5DM8MGD98; _abck=475CA93F4E29A2390706DD9FAB240A9F172DB63E1B440000D3CE975C812CEC01~0~lQzDpVECn4msKe2gkBPG5bP1iDb8SDWYr6EAFdnJ4Ww=~-1~-1; _ga=GA1.2.1138836386.1553452762; _gid=GA1.2.1539230976.1553452762; AMCVS_371C27E253DB0F910A490D4E%40AdobeOrg=1; _gcl_au=1.1.1693472285.1553452762; AMCV_371C27E253DB0F910A490D4E%40AdobeOrg=1278862251%7CMCIDTS%7C17980%7CMCMID%7C03890195065185467251056867340607034585%7CMCAAMLH-1554057562%7C7%7CMCAAMB-1554057562%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1553459962s%7CNONE%7CMCAID%7C2E4BE76D05079629-4000010660000BC5%7CvVersion%7C4.0.0; s_cc=true; undefined_s=First%20Visit; AKA_A2=A; dtLatC=1; dtSa=-; DivisionID=620; StoreCode=00008; StoreZipCode=80129; StoreLocalName=King%20Soopers; StoreAddress=2205%20W%20Wildcat%20Reserve%20Pkwy%2C%20Highlands%20Ranch%2C%20CO; StoreInformation=2205%20W%20Wildcat%20Reserve%20Pkwy%2C%20Highlands%20Ranch%2C%20CO%2C7203444503%2C%207203440334; s_ppvl=bn%253Asearch%253Aproducts%2C100%2C100%2C1180%2C1953%2C1180%2C2560%2C1440%2C1%2CP; XSRF-TOKEN=858631f4-5c66-4049-a28d-cd57c7aed547; __VCAP_ID__=e5871a89-99ec-4e3c-7f17-475c; dtCookie=4$49E9A29F5EF3F1D47201A20F78E239F3|81222ad3b2deb1ef|1; s_ppv=bn%253Asearch%253Aproducts%2C98%2C98%2C1180%2C902%2C1180%2C2560%2C1440%2C1%2CPL; s_nr=1553456902953-Repeat; s_sq=%5B%5BB%5D%5D; bm_sv=9DD040A9C6740ADD5FDC51C22AD2711C~ILJsVUeAT0FrEe/rHQN5omFiaTaPNtFhIgh8E7rlfu3mpbxNBmtALEBdk7MLqjMa5grKt/K/NzfnhwtyHO3R4NuMCj4gwkhfP5sxhtlcsKvSmgMM5n0LVYxT4lmNO9oyQq9/k4YcHLJdJa4tnsYZOyJQLgHRPyza3vTEabncMDI=; rxvt=1553458703599|1553452760669; dtPC=4$56873826_321h30vFMIKNHLJDNIFJAJBEGFDOEAIBPMHGKKG

    '''

    def start_requests(self):
        yield scrapy.Request(url='https://www.kingsoopers.com/products/api/products/details',
                             method='POST',
                             body=self.payload, 
                             headers={'content-type':'application/json','x-xsrf-token':'858631f4-5c66-4049-a28d-cd57c7aed547','x-dtreferer':'https://www.kingsoopers.com/search?tab=0&page=1&searchType=curated','cookie':self.reqCookie,'store-id':'00008','division-id':'620'},
                             callback=self.parse_products)

    def parse_products(self,response):

        data = json.loads(response.body)

        with open('sample.json','w') as file:

            file.write(json.dumps(data))

