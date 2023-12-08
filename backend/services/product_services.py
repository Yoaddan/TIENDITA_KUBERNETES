from logger.logger_base import log
from flask import jsonify

class ProductService:
    def __init__(self, db_connector):
        self.db_connector = db_connector

    def get_all_products(self):
        try:
            products = list(self.db_connector.db.productos.find())
            return products
        except Exception as e:
            log.critical(f'Error fetching all products from the database: {e}')
            return jsonify({'error': f'Error fetching all products from the database: {e}'}), 500

    def get_product_by_name(self, product_name):
        try:
            product = self.db_connector.db.productos.find_one({'nombre': product_name})
            return product
        except Exception as e:
            log.critical(f'Error fetching the product by name from the database: {e}')
            return jsonify({'error': f'Error fetching the product by name from the database: {e}'}), 500

    def get_products_by_category(self, category):
        try:
            products = list(self.db_connector.db.productos.find({'categoria': category}))
            return products
        except Exception as e:
            log.critical(f'Error fetching products by category from the database: {e}')
            return jsonify({'error': f'Error fetching products by category from the database: {e}'}), 500

    def get_products_by_price(self, price):
        try:
            products = list(self.db_connector.db.productos.find({'precio': {'$lte': price}}))
            return products
        except Exception as e:
            log.critical(f'Error fetching products by price from the database: {e}')
            return jsonify({'error': f'Error fetching products by price from the database: {e}'}), 500
