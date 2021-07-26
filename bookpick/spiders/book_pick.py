import scrapy
from ..items import BookpickItem

class BookPickSpider(scrapy.Spider):
    name = 'book_pick'
    start_urls = ['https://reedsy.com/discovery/blog/best-self-help-books']

    def parse(self, response):
        items = BookpickItem()
        book = response.css('h3 em::text').extract()
        for i in range(len(book)):
            items['book'] = book[i]
            yield items
