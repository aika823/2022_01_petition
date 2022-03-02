import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petition.settings')
application = get_wsgi_application()
# application = WhiteNoise(application, root='/web/petition')
# application.add_files('/web/petition/static/', prefix='')