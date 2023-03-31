from pathlib import Path

DEBUG = True

INSTALLED_APPS = [
    "material",
    "material.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'actors',
    'cadres',
    'categories',
    'genre',
    'movies',
    'ratings',
    'reviews',
]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent.parent / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         "NAME": "postgres",
#         "USER": "postgres",
#         "PASSWORD": "nurma",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }
