import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME', 'team_management'),
        'USER': os.getenv('DATABASE_USER', 'admin'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'instateam'),
        'HOST': os.getenv('DATABASE_HOST', 'db'),  # The name of the MySQL service in docker-compose
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
