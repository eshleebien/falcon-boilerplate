from controllers import *

class Router:
    def __init__(self, app):
        app.add_route('/', Request.Resource())
        app.add_route('/callback', Callback.Resource())
