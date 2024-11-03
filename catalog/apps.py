from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials
import os


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'

    def ready(self):
        # Only initialize Firebase once
        if not firebase_admin._apps:
            # Use the environment variable you set for the credentials
            cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
            firebase_admin.initialize_app(cred , {
                'storageBucket': 'rastro-images.appspot.com'
            })