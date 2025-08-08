# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksScraperItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    availability = scrapy.Field()
    img_source = scrapy.Field()
    link = scrapy.Field()
    # genre = scrapy.Field()
    # desc = scrapy.Field()
    # upc = scrapy.Field()
