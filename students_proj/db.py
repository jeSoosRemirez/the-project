DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': str(BASE_DIR / 'db.sqlite3'),
        'NAME': 'studentsdb',
        'USER': 'studentsdb',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '',
    }
}
