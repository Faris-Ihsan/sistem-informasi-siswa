import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'app.py')
application = wsgi.app
application.secret_key = os.getenv('SECRET_KEY', 'for dev') 