# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class PetlebiproductsPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='malatya44',
            database='petlebi_products'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS petlebi""")
        self.curr.execute("""CREATE TABLE petlebi (
                            product_id INT,
                            product_url TEXT,
                            product_name TEXT,
                            product_price TEXT,
                            product_stock TEXT,
                            product_images TEXT,
                            product_category TEXT,
                            product_brand TEXT
                            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO petlebi VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", (
            item['product_id'][0],
            item['product_url'][0],
            item['product_name'][0],
            item['product_price'][0],
            item['product_stock'][0],
            item['product_images'][0],
            item['product_category'][0],
            item['product_brand'][0]
        ))

        self.conn.commit()