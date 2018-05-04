# Local settings
from data_ui.settings import *

DATABASES['datadrop_business'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': '',
    'HOST': '',
    'USER': '',
    'PASSWORD': ''
}

# For production, override these things:
SECRET_KEY = 'CUSTOM KEY HERE'
DEBUG = True
