from django.apps import AppConfig
from django.contrib.admin import apps



class Admin_edu(apps.AdminConfig):
    default_site='edu_app.admin.Edu_admin'




class EduAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edu_app'
    verbose_name="البرامج التعليميه"
