import os

from django.conf import settings


engines = {
    'sqlite': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql_psycopg2',
    'mysql': 'django.db.backends.mysql',
}


def config():
    service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper().replace('-', '_')
    if service_name:
        engine = engines.get(os.getenv('DATABASE_ENGINE'), engines['sqlite'])
    else:
        engine = engines['sqlite']
    name = os.getenv('DATABASE_NAME')
    if not name and engine == engines['sqlite']:
        name = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    return {
        'ENGINE': engine,
        'NAME': name,
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
