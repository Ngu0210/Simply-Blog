from flask import Blueprint, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

swag = Blueprint("swagger", __name__)

@swag.route('/static/<path:path>')
def send_swag(path):
    return send_from_directory('static', path)

SWAGGER_URL = '/swagger'
API_URL = 'static/swagger.json'


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': "Simply-Blog"
    }
)