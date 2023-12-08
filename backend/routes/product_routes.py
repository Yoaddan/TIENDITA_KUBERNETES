from flask import Blueprint, jsonify, request
from logger.logger_base import log
from marshmallow import ValidationError

class ProductRoutes(Blueprint):
    def __init__(self, product_service, product_schema):
        super().__init__('product', __name__)
        self.product_service = product_service
        self.product_schema = product_schema
        self.register_routes()

    def register_routes(self):
        self.route('/api/products', methods=['GET'])(self.get_all_products)
        self.route('/api/products/<string:product_name>', methods=['GET'])(self.get_product_by_name)
        self.route('/api/products/category/<string:category>', methods=['GET'])(self.get_products_by_category)
        self.route('/api/products/price/<int:price>', methods=['GET'])(self.get_products_by_price)

    def get_all_products(self):
        try:
            products = self.product_service.get_all_products()
            return jsonify(products), 200
        except Exception as e:
            log.exception(f'Error fetching data from the database: {e}')
            return jsonify({'error': 'Failed to fetch data from the database'}), 500

    def get_product_by_name(self, product_name):
        product = self.product_service.get_product_by_name(product_name)
        if product:
            return jsonify(product), 200
        else:
            return jsonify({'error': 'Product not found'}), 404

    def get_products_by_category(self, category):
        try:
            products = self.product_service.get_products_by_category(category)
            return jsonify(products), 200
        except Exception as e:
            log.exception(f'Error fetching data from the database: {e}')
            return jsonify({'error': 'Failed to fetch data from the database'}), 500

    def get_products_by_price(self, price):
        try:
            products = self.product_service.get_products_by_price(price)
            return jsonify(products), 200
        except Exception as e:
            log.exception(f'Error fetching data from the database: {e}')
            return jsonify({'error': 'Failed to fetch data from the database'}), 500