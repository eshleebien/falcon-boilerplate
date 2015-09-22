Falcon boilerplate
====
*WIP*

How to setup
-------------------
Create your local configuration by copying the example configuration from config/example_config.py
```sh
cd config
cp example_config.py development.py
vi development.py
```

Modify it according to your local environment settings

--------------------
Run the command/s below once or everytime you add packages

```sh
pip3 install -r requirements.txt
```

How to run
----------------
```sh
APP_ENV=development gunicorn app:app
```

Project Structure
--------------
        - config
                - __init__.py
                - routes.py
                - example_config.py
        - controllers
                - __init__.py
                - Callback.py
                - Request.py
        - threads
                - __init__.py
                - master.py
                - client.py
        - util
                - helpers.py
                - sqs.py
        - app.py
        - requirements.py

------------------

```
config directory - contains file for configurations and routes register
controller directory - contains classes that handles the route registered in the config/routes.py file
threads directory - contains the threaded events used for fetching data from different data sources and other intensive calculations
util directory - contains all the helper classes
app.py - Initializes the application

