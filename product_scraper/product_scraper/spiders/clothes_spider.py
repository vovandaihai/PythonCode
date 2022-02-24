import scrapy
from ..items import ProductScraperItem
import re
import json

class ClothesSpider(scrapy.Spider):
    name = 'Ao'
    start_urls= ['https://dunlopsports.com.vn/thoi-trang-nam-01']
    firstLink = 'https://dunlopsports.com.vn'
    pageNumber = 1
    pageEnd = 6
    links = []
    
    def parse(self, response):
        next_page = "https://dunlopsports.com.vn/thoi-trang-nam-01?q=collections:1766182&page=" + str(ClothesSpider.pageNumber) + "&view=grid"
        for products in response.css('a.btn-fill'):
            ClothesSpider.link = ClothesSpider.firstLink + products.attrib['href']
            ClothesSpider.links.append(ClothesSpider.link)
        
        
        if ClothesSpider.pageNumber <= ClothesSpider.pageEnd:
            ClothesSpider.pageNumber = ClothesSpider.pageNumber + 1
            yield response.follow(next_page, callback = self.parse)

       
        for link in ClothesSpider.links:
            yield response.follow (link, callback = self.fill_data)
        
    def fill_data (self, response):
        items = ProductScraperItem()
        data = re.findall("product: {(.+?);\n", response.body.decode("utf-8"), re.S)
        finalData = "{" + data[0][:data[0].find("content")-2] + "}"
        finalDictData = json.loads(finalData)
        items['id'] = finalDictData['id']
        items['name'] = finalDictData['name']
        items['price'] = finalDictData['compare_at_price_max']
        items['salePrice'] = finalDictData['price_min']
        d = []
        for image in finalDictData['images']:
            d.append(image['src'])
        items['images']=d
        s = set()
        c = set()
        for variant in finalDictData['variants']:
            if variant['available'] == True:
                if len(variant['options']) == 2:
                    s.add(variant['option2'])
                    c.add(variant['option1'])
                else:
                    s.add(variant['option1'])
        items['size'] = s
        items['color'] = c       
        items['link'] = response.css('meta[property="og:url"]').attrib['content']
        items['description'] = response.css('meta[name="description"]').attrib['content']
        yield items