import scrapy
from ..items import BooksScraperItem

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        all_div_books = response.css('article.product_pod')

       

        for book in all_div_books:

            items = BooksScraperItem()

            name = book.css('.product_pod h3 a::attr(title)').extract_first()
            price = book.css('.price_color::text').extract_first()
            availability = book.css('.availability::text').extract()[-1].strip()
            img_source = "https://books.toscrape.com/" + book.css('.thumbnail::attr(src)').extract_first()
            url = "https://books.toscrape.com/" + book.css('.image_container a::attr(href)').extract_first()
            rating = book.css('.star-rating::attr(class)').extract_first().split()[-1]


            items['name'] = name
            items['price'] = price
            items['availability'] = availability
            items['img_source'] = img_source
            items['link'] = url
            items['rating'] = rating
             
            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)