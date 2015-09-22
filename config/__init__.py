import os


app_env = os.environ.get('APP_ENV', 'development')
config = getattr(__import__('config', fromlist=[app_env]), app_env)

print(' * ' + app_env + ' configuration files loaded')
