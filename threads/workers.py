import multiprocessing
import threading
import time

# from threads import client
# from config import config
# from util import sqs


def worker():
    # if threading.active_count() >= config.max_thread_count:
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(10)
    print(name, 'Exiting')


jobs = []
for i in range(5):
    worker = multiprocessing.Process(name='my_worker', target=worker)
    jobs.append(worker)
    worker.start()

print(jobs)
