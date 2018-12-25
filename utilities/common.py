from time import time

import boto3
from flask import current_app

from settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION_NAME


def utc_now_timestamp():
    return int(time())


def email(to_email, subject, body_html, body_txt):
    # don't run this if we're running a test
    if current_app.config.get('TESTING'):
        return False

    client = boto3.client('ses',
                          aws_access_key_id=AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name=AWS_REGION_NAME,
                          )
    return client.send_email(
        Source='matveykhvatov@gmail.com',
        Destination={
            'ToAddresses': [
                to_email,
            ]
        },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': body_txt,
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': body_html,
                    'Charset': 'UTF-8'
                },
            }
        }
    )
