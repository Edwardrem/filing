import os

bind = 'localhost:8000'
workers = 3
worker_class = 'sync'
loglevel = 'info'
accesslog = '-'
errorlog = '-'
proc_name = 'prince_shipping_system'
pythonpath = os.path.dirname(os.path.abspath(__file__))