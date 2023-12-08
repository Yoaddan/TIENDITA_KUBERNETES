from flask import Flask
from models.product_models import ProductModel
from flask_swagger_ui import get_swaggerui_blueprint
from services.product_services import ProductService
from routes.product_routes import ProductRoutes
from schemas.product_schemas import ProductSchema
from flask_cors import CORS

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Ferreteria API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

db_connector = ProductModel()
db_connector.connect_to_database()

product_service = ProductService(db_connector)
product_schema = ProductSchema()

product_blueprint = ProductRoutes(product_service, product_schema)
app.register_blueprint(product_blueprint)

CORS(app, resources={r'/api/products': {'origins': '*'}})

if __name__ == '__main__':
    try:
        app.run(debug=True)
    finally:
        db_connector.close_connection()
