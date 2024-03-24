import scrapy
import json

from ..items import PetlebiproductsItem


class PetlebiSpiderSpider(scrapy.Spider):
    name = "petlebi_spider"
    page_number = 2
    start_urls = [
        "https://www.petlebi.com/kedi-mamasi?page=1",
        "https://www.petlebi.com/kedi-konserve-mamasi?page=1",
        "https://www.petlebi.com/kedi-konserve-mamasi?page=1",
        "https://www.petlebi.com/kedi-vitamin-ve-ek-besinleri?page=1",
        "https://www.petlebi.com/kedi-kumu?page=1",
        "https://www.petlebi.com/kedi-tuvaleti?page=1",
        "https://www.petlebi.com/kedi-oyuncaklari?page=1",
        "https://www.petlebi.com/kedi-tirmalama-tahtasi?page=1",
        "https://www.petlebi.com/kedi-mama-ve-su-kabi?page=1",
        "https://www.petlebi.com/kedi-kapisi?page=1",
        "https://www.petlebi.com/kedi-tasmasi?page=1",
        "https://www.petlebi.com/kedi-yataklari?page=1",
        "https://www.petlebi.com/kedi-tasima-cantasi?page=1",
        "https://www.petlebi.com/kedi-evi?page=1",
        "https://www.petlebi.com/kedi-sampuani?page=1",
        "https://www.petlebi.com/kedi-bakim-urunleri?page=1",
        "https://www.petlebi.com/kedi-tarak-ve-fircalari?page=1",
        "https://www.petlebi.com/kedi-cimi?page=1",
        "https://www.petlebi.com/kedi-otu?page=1",
        "https://www.petlebi.com/kedi-uzaklastirici-sprey?page=1",
        "https://www.petlebi.com/kedi-pire-kene-urunleri?page=1",
        "https://www.petlebi.com/kopek-mamasi?page=1",
        "https://www.petlebi.com/kopek-konserve-mamasi?page=1",
        "https://www.petlebi.com/kopek-odul-mamasi?page=1",
        "https://www.petlebi.com/kopek-kemigi?page=1",
        "https://www.petlebi.com/kopek-vitamin-ve-ek-besini?page=1",
        "https://www.petlebi.com/kopek-oyuncaklari?page=1",
        "https://www.petlebi.com/kopek-yataklari?page=1",
        "https://www.petlebi.com/kopek-mama-ve-su-kabi?page=1",
        "https://www.petlebi.com/kopek-tasmalari-kayislari?page=1",
        "https://www.petlebi.com/kopek-tasima-cantasi?page=1",
        "https://www.petlebi.com/kopek-elbiseleri?page=1",
        "https://www.petlebi.com/egitim-ekipmani?page=1",
        "https://www.petlebi.com/kopek-kulubesi?page=1",
        "https://www.petlebi.com/kopek-araba-urunleri?page=1",
        "https://www.petlebi.com/kopek-bahce-urunleri?page=1",
        "https://www.petlebi.com/kopek-bakim-urunleri?page=1",
        "https://www.petlebi.com/kopek-tarak-ve-fircasi?page=1",
        "https://www.petlebi.com/kopek-sampuani?page=1",
        "https://www.petlebi.com/kopek-parfumu?page=1",
        "https://www.petlebi.com/kopek-uzaklastirici-sprey?page=1",
        "https://www.petlebi.com/kopek-paraziter-pire-kene-engelleyici?page=1",
        "https://www.petlebi.com/kus-yemleri?page=1",
        "https://www.petlebi.com/kus-kafesleri?page=1",
        "https://www.petlebi.com/kus-oyuncaklari?page=1",
        "https://www.petlebi.com/kus-yuvalari?page=1",
        "https://www.petlebi.com/kus-kumu?page=1",
        "https://www.petlebi.com/kus-bakim-urunleri?page=1",
        "https://www.petlebi.com/kus-vitaminleri-saglik-urunleri?page=1",
        "https://www.petlebi.com/kus-gaga-taslari?page=1",
        "https://www.petlebi.com/kus-krakeri-ve-odulleri?page=1",
        "https://www.petlebi.com/kus-kafesi-ekipmanlari?page=1",
        "https://www.petlebi.com/kemirgen-petshop-urunleri?page=1",

    ]

    def parse(self, response):

        items = PetlebiproductsItem()

        all_div_products = response.css('.search-product-box')

        for products in all_div_products:
            product_url= products.css('a ::attr(href)').extract()
            product_name = products.css('h3.commerce-title::text').extract()
            product_price = products.css('.commerce-discounts::text').extract()
            product_stock = products.css('a.p-link::attr(data-gtm-product)').re_first(r'"dimension2":"(.*?)"')
            product_images = products.css('.mb-2::attr(data-original)').extract()
            product_category = products.css('a.p-link::attr(data-gtm-product)').re_first(r'"category":"(.*?)"')
            product_id = products.css('div.card-body.pb-0.pt-2.pl-3.pr-3::attr(data-id)').extract_first()
            product_brand = products.css('a.p-link::attr(data-gtm-product)').re_first(r'"brand":"(.*?)"')

            items['product_url'] = product_url
            items['product_name'] = product_name
            items['product_price'] = product_price
            items['product_stock'] = product_stock
            items['product_images'] = product_images
            items['product_category'] = product_category
            items['product_id'] = product_id
            items['product_brand'] = product_brand
            yield items

        next_page = response.css('.page-item.active + .page-item a::attr(href)').extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)



