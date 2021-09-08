from .base import * 

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'prueba',
        'USER': 'Rata',
        'PASSWORD':'a',
        'HSOT': 'localhost',
        'PORT': '5432'
    }
}
