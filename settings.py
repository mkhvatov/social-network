import os

import secrets


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'yEe5JjegFnuxdh}3ZSM9'
HOST = '0.0.0.0'
PORT = 5000
HOSTNAME = f'http://{HOST}:{PORT}'

MONGODB_SETTINGS = {
    'db': os.getenv('MONGODB_NAME', 'flaskbook'),
    'host': os.getenv('MONGODB_HOST', 'db'),
    'port': os.getenv('MONGODB_PORT', 27017)
}

# todo:
STATIC_IMAGE_URL = ''
AWS_BUCKET = ''
AWS_CONTENT_URL = ''
UPLOAD_FOLDER = ''
AWS_ACCESS_KEY_ID = secrets.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = secrets.AWS_SECRET_ACCESS_KEY
AWS_REGION_NAME = secrets.AWS_REGION_NAME
