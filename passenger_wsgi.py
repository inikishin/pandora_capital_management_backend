# file for reg.ru hosting
import os, sys
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/var/www/u1016303/data/www/api.pandoracapitalmanagement.ru/pandora_capital_management_backend/')
sys.path.insert(1, '/var/www/u1016303/data/prenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pandora_capital_management_backend.settings'
application = get_wsgi_application()
