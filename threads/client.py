import threading
import time

from config import config
from util import sqs


class ClientThread(threading.Thread):
    def __init__(self, s_name, d_channel):
        threading.Thread.__init__(self)
        self.s_name = s_name
        self.d_channel = d_channel

    def run(self):
        # if threading.active_count() >= config.thread_count:
        if threading.active_count() <= config.thread_count:

            d_message_body = {
                'channel_id': {
                    'StringValue': self.d_channel['channel_id'],
                    'DataType': 'String'
                },
                'type': {
                    'StringValue': self.d_channel['type'],
                    'DataType': 'String'
                },
                'metrics': {
                    'StringValue': ','.join(self.d_channel['metrics']),
                    'DataType': 'String'
                },
                'source': {
                    'StringValue': self.d_channel['source'],
                    'DataType': 'String'
                },
                'user': {
                    'StringValue': self.d_channel['user'],
                    'DataType': 'String'
                },
                'time': {
                    'StringValue': str(self.d_channel['timestamp']),
                    'DataType': 'String'
                }
            }

            sqs_instance = sqs.SQS(config.AWS['SQS'])
            sqs_instance.set_queue('snji_thread_queue')

            response = sqs_instance.send_message('thread-' +
                                          self.d_channel['channel_id'],
                                          d_message_body)

            print('queued process')
            print(response)

        else:
            print('Starting client thread ' + str(threading.active_count()))

            time.sleep(10)

            print('End client thread ' + self.s_name)

