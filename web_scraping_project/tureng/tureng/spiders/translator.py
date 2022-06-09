import scrapy
from tureng.items import TurengItem
from scrapy.loader import ItemLoader

class translatorSpider(scrapy.Spider):
    name = "translate"

    def start_requests(self):
        yield scrapy.Request(f'https://tureng.com/en/turkish-english/{self.word}')

    def parse(self, response):
        for words in response.css('table.table-hover.table-striped.searchResultsTable').css('tr'):
            load = ItemLoader(item = TurengItem(), selector = words)

            load.add_css('word', 'td.en.tm')
            load.add_css('resp', 'td.tr.ts')

            yield load.load_item()
            