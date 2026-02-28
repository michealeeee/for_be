from django.apps import AppConfig
from mongoengine import connect


class BeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'be_app'

    def ready(self):
        connect(db='be',
                    host='mongodb+srv://mke00007_db_user:ofLjBkXKyzGZgYKJ@beprojectdb.vs6rvei.mongodb.net/?appName=be', )
