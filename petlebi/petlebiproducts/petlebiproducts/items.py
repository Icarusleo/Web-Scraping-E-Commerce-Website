# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PetlebiproductsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_url = scrapy.Field()
    product_name = scrapy.Field()
    product_barcode = scrapy.Field()
    product_price = scrapy.Field()
    product_stock = scrapy.Field()
    product_images = scrapy.Field()
    product_description = scrapy.Field()
    product_sku = scrapy.Field()
    product_category = scrapy.Field()
    product_id = scrapy.Field()
    product_brand = scrapy.Field()

