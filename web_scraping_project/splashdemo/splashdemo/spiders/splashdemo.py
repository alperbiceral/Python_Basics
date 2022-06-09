import scrapy
from scrapy_splash import SplashRequest

class SplashDemo(scrapy.Spider):
    name = 'splash'

    def start_requests(self):
        yield SplashRequest(url='https://www.beerwulf.com/en-gb/c/mixedbeercases', callback=self.parse)

    def parse(self, response):
        for item in response.css('a.product.search-product.draught-product.notranslate.pack-product'):
            yield {
                'name': item.css('h4::text').get(),
                'price': item.css('span.price::text').get().replace('£ ',''),
                'remaining': item.css('p::text').get()
            }