import os
import sys

# Project path
PROJECT_PATH = '/home/hightech/r3.quantumcoresoftware.com/home'
if PROJECT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_PATH)

# Virtualenv site-packages path
VENV_SITE_PACKAGES = '/home/hightech/virtualenv/r3.quantumcoresoftware.com/home/3.10/lib/python3.10/site-packages'
if VENV_SITE_PACKAGES not in sys.path:
    sys.path.insert(0, VENV_SITE_PACKAGES)

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

# Load application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()