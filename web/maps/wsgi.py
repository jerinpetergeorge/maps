import time
import traceback
import signal
import sys
import pathlib
from django.core.handlers.wsgi import WSGIHandler
import os

# add the hellodjango project path into the sys.path
#sys.path.append('<PATH_TO_MY_DJANGO_PROJECT>/hellodjango')
sys.path.append(pathlib.Path(__file__).parent.parent.parent.absolute())

# add the virtualenv site-packages path to the sys.path
sys.path.append('/var/www/html/web/venv/lib/python3.6/site-packages')

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maps.settings")

from django.core.wsgi import get_wsgi_application

#sys.path.append(pathlib.Path(__file__).parent.parent.parent.absolute())
# adjust the Python version in the line below as needed
#sys.path.append('/var/www/html/web/venv/lib/python3.6/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maps.settings')
#os.environ['DB_NAME'] = "maps_data"
#os.environ['DB_USER'] = "chicommons"
#os.environ['DB_PASS'] = "ChiCommons1$"
#os.environ['DB_SERVICE'] = "localhost"
#os.environ['DB_PORT'] = "3306"

try:
    application = get_wsgi_application()
except Exception:
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)



