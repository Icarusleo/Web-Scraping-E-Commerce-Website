import mysql.connector
import json

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="petlebi_products"
)
cursor = mydb.cursor()

with open('petlebi_products.json', encoding='utf-8') as f:

    for line in f:
        try:

            product = json.loads(line)

            product_url = product['product_url'][0]
            product_name = product['product_name'][0]

            product_price = product['product_price'][0]
            if product_price:

                product_price = float(''.join(filter(str.isdigit, product_price))) / 100
            else:
                product_price = None

            product_stock = product['product_stock']
            product_images = product['product_images'][0]
            product_category = product['product_category']
            product_id = product['product_id']
            product_brand = product['product_brand']

            sql = "INSERT INTO petlebi (product_url, product_name, product_price, product_stock, product_images, product_category, product_id, product_brand) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (product_url, product_name, product_price, product_stock, product_images, product_category, product_id, product_brand)
            cursor.execute(sql, val)

        except json.JSONDecodeError as e:

            print(f"Error parsing JSON: {e}")
            continue

        except KeyError as e:

            print(f"KeyError: {e}")
            continue


mydb.commit()
mydb.close()
