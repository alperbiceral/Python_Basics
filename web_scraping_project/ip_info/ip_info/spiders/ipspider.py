import scrapy
from ip_info.items import IpInfoItem
from scrapy.loader import ItemLoader

class IpSpider(scrapy.Spider):
    name = 'ip_info'

    def start_requests(self):
        yield scrapy.Request(f'https://ip-46.com/{self.ip}')

    def parse(self, response):
        for info in response.css('div.mr5.cb'):
            load = ItemLoader(item = IpInfoItem(), selector = info)

            load.add_css('text', 'div.f7.b.ml0.mt1.fw4.code.mt2')

            yield load.load_item()
