import falcon
import json

from util import sqs
from config import config


class Resource:
    def on_get(self, req, resp):
        s_channel_id = req.get_param('channel_id', True)
        l_metrics = req.get_param_as_list('metrics', str, True)
        s_type = req.get_param('type', True)
        s_source = req.get_param('source', True)
        s_user = req.get_param('user', True)
        timestamp = req.get_param_as_int('timestamp', True)

        d_message_body = {
            'channel_id': {
                'StringValue': s_channel_id,
                'DataType': 'String'
            },
            'type': {
                'StringValue': s_type,
                'DataType': 'String'
            },
            's3_url': {
                'StringValue': 'link_here',
                'DataType': 'String'
            },
            'metrics': {
                'StringValue': l_metrics,
                'DataType': 'String'
            },
            'source': {
                'StringValue': s_source,
                'DataType': 'String'
            },
            'user': {
                'StringValue': s_user,
                'DataType': 'String'
            },
            'time': {
                'StringValue': str(timestamp),
                'DataType': 'String'
            }
        }

        queue = sqs.SQS(config.AWS['SQS'])
        response = queue.send_message(s_type + '-' + s_channel_id
                                      + '-' + str(timestamp), d_message_body)

        resp.status = falcon.HTTP_200
        resp.body = (json.dumps(response))
