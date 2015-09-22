import threading
# import time

# from threads import client
from config import config
from util import sqs


class WorkerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i_threadID = 1
        self.s_name = 'master'
        self.i_thread_count = 0

    def run(self):
        while True:
            if threading.active_count() < config.thread_count:
                queue = sqs.SQS(config.AWS['SQS'])
                queue = sqs.set_queue('snji_thread_queue')
                result = queue.receive_message(['all'], ['string'],
                                               1, 123, 123)

                # p = client.ClientThread('child-thread-' + 'UC-TEST',
                #        {'channel_id': 'UC-TEST'})
                # p.start()
