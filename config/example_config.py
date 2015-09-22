import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

APP_NAME = 'Falcon'

AWS = {
    'SQS': {
        'ACCESS_KEY': 'key here',
        'SECRET_ACCESS_KEY': 'secret here',
        'REGION': 'us-east-1',
        'PRIORITY_QUEUE': 'Snji-priority-test',
        'DEFAULT_QUEUE': 'Snji-default-test',
    }
}
