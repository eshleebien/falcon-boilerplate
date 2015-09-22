import falcon
import json
import time

from threads import client


class Resource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nNothing to do here\n\n')

    def on_post(self, req, resp):
        s_channel_id = req.get_param('channel_id', True)
        l_metrics = req.get_param_as_list('metrics', str, True)
        s_type = req.get_param('type', True)
        s_source = req.get_param('source', True)
        s_user = req.get_param('user', True)
        timestamp = int(round(time.time() * 1000))
        response = {}

        d_channel = {
            'channel_id': s_channel_id,
            'metrics': l_metrics,
            'type': s_type,
            'source': s_source,
            'user': s_user,
            'timestamp': timestamp
        }
        # start fetching data here
        thread = client.ClientThread('thread-uc-test', d_channel)
        thread.start()

        resp.status = falcon.HTTP_200
        resp.body = (json.dumps(response))
