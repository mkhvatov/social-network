import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'yEe5JjegFnuxdh}3ZSM9'

DATABASE = {
    'user': os.getenv('MONGODB_USER', None),
    'password': os.getenv('MONGODB_PASSWD', None),

    'host': os.getenv('MONGODB_HOST', 'db'),
    'port': os.getenv('MONGODB_PORT', 27017),
    'name': os.getenv('MONGODB_NAME', 'flaskbook')
}
DATABASE['authDb'] = os.getenv('MONGODB_AUTHDB', DATABASE['name'])

# todo:
STATIC_IMAGE_URL = ''
AWS_BUCKET = ''
AWS_CONTENT_URL = ''
UPLOAD_FOLDER = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_REGION_NAME = ''
